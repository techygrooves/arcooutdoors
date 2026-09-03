#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Technical SEO guard. Python 3 stdlib only; nothing here runs at deploy time.

Checks every .html page in the repository against the metadata contract in
PROJECT-SPEC.md §8.7, plus heading structure, structured data and the sitemap.
Exits non-zero on any breach, so it can sit beside sync-partials.py --check and
check-links.py as a pre-commit guard.

    python3 tools/audit-seo.py            # from the repository root

What it will not let past:
  * a missing, duplicated or over-long title or meta description
  * a missing canonical, viewport, charset, robots or Open Graph/Twitter tag
  * a page with zero or several <h1>, or a heading level skipped on the way down
  * JSON-LD that does not parse, or an @id reference nothing declares
  * fabricated business claims in structured data (see FORBIDDEN below)
  * a sitemap entry with no page behind it, or a page missing from the sitemap
"""
import json, os, re, sys, collections
from html.parser import HTMLParser

DOMAIN = 'https://www.arcooutdoors.com/'
TITLE_MAX, DESC_MIN, DESC_MAX = 62, 110, 160
ROBOTS_OK = 'index, follow, max-image-preview:large'

# Properties that would assert something about the business no source material
# supports. §3 and §12: no rating or review exists, no price, no founding date,
# no headcount, no surveyed coordinates. Adding any of these is fabrication, so
# it fails the build rather than shipping quietly.
FORBIDDEN = ('aggregateRating', 'ratingValue', 'reviewCount', 'priceRange',
             'foundingDate', 'numberOfEmployees', 'geo', 'latitude', 'longitude')

REQUIRED_META = ('description', 'viewport', 'robots', 'og:type', 'og:site_name',
                 'og:locale', 'og:title', 'og:description', 'og:url', 'og:image',
                 'og:image:width', 'og:image:height', 'og:image:alt',
                 'twitter:card', 'twitter:title', 'twitter:description',
                 'twitter:image', 'twitter:image:alt')


class Head(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta, self.link, self.title, self._t, self.charset = {}, {}, None, False, False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta':
            if 'charset' in a:
                self.charset = True
            key = a.get('name') or a.get('property')
            if key:
                self.meta[key.lower()] = (a.get('content') or '').strip()
        elif tag == 'link':
            rel = (a.get('rel') or '').lower()
            if rel:
                self.link[rel] = a.get('href')
        elif tag == 'title':
            self._t = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self._t = False

    def handle_data(self, data):
        if self._t:
            self.title = (self.title or '') + data


def pages():
    out = []
    for dirpath, _, files in os.walk('.'):
        if '/.git' in dirpath or 'partials' in dirpath:
            continue
        out += [os.path.relpath(os.path.join(dirpath, f), '.')
                for f in files if f.endswith('.html')]
    return sorted(out)


def main():
    errors, seen = [], collections.defaultdict(list)
    ids, refs = set(), []

    for page in pages():
        raw = open(page, encoding='utf-8').read()
        head = Head()
        head.feed(raw.split('</head>')[0])
        meta, err = head.meta, lambda m: errors.append('%s: %s' % (page, m))
        noindex = 'noindex' in meta.get('robots', '')
        title = (head.title or '').strip()

        if not head.charset:
            err('no <meta charset>')
        if not title:
            err('no <title>')
        elif len(title) > TITLE_MAX:
            err('title is %d characters (max %d)' % (len(title), TITLE_MAX))

        # An error page is deliberately exempt from everything below.
        if noindex:
            continue

        seen['title'].append((title, page))
        canonical = head.link.get('canonical')
        if not canonical:
            err('no canonical')
        elif not canonical.startswith(DOMAIN):
            err('canonical does not name the production domain: %s' % canonical)
        else:
            seen['canonical'].append((canonical, page))

        for key in REQUIRED_META:
            if not meta.get(key):
                err('no %s' % key)

        desc = meta.get('description', '')
        if desc:
            seen['description'].append((desc, page))
            if not DESC_MIN <= len(desc) <= DESC_MAX:
                err('description is %d characters (want %d-%d)'
                    % (len(desc), DESC_MIN, DESC_MAX))
        if meta.get('robots') and meta['robots'] != ROBOTS_OK:
            err('robots is %r, expected %r' % (meta['robots'], ROBOTS_OK))
        # og:description may deliberately differ from the meta description -- a
        # share blurb and a search snippet are read in different places and
        # fourteen pages use that on purpose. What must never differ is the
        # Open Graph and Twitter pair, which describe the same card.
        if meta.get('twitter:description') != meta.get('og:description'):
            err('twitter:description does not match og:description')
        if meta.get('twitter:title') != meta.get('og:title'):
            err('twitter:title does not match og:title')
        if meta.get('og:url') and meta['og:url'] != canonical:
            err('og:url does not match the canonical')
        if meta.get('twitter:image') and meta['twitter:image'] != meta.get('og:image'):
            err('twitter:image does not match og:image')
        card = (meta.get('og:image') or '').replace(DOMAIN, '')
        if card and not os.path.isfile(card):
            err('og:image has no file behind it: %s' % card)

        body = re.sub(r'<!--.*?-->', '', raw.split('</head>')[-1], flags=re.S)
        levels = [(int(m.group(1)), re.sub(r'<[^>]+>', '', m.group(2)).strip()[:48])
                  for m in re.finditer(r'<h([1-6])[^>]*>(.*?)</h\1>', body, re.S | re.I)]
        h1 = [x for x in levels if x[0] == 1]
        if len(h1) != 1:
            err('%d <h1> elements, expected exactly 1' % len(h1))
        previous = 0
        for level, text in levels:
            if previous and level > previous + 1:
                err('heading jumps h%d to h%d at %r' % (previous, level, text))
            previous = level

        for block in re.finditer(r'application/ld\+json[^>]*>(.*?)</script>', raw, re.S):
            text = block.group(1)
            try:
                data = json.loads(text)
            except ValueError as exc:
                err('JSON-LD does not parse: %s' % exc)
                continue
            for prop in FORBIDDEN:
                if '"%s"' % prop in text:
                    err('structured data asserts %r, which no source material '
                        'supports (see PROJECT-SPEC.md §12)' % prop)

            def walk(node):
                if isinstance(node, dict):
                    if '@type' in node and '@id' in node:
                        ids.add(node['@id'])
                    if set(node) == {'@id'}:
                        refs.append((page, node['@id']))
                    for value in node.values():
                        walk(value)
                elif isinstance(node, list):
                    for value in node:
                        walk(value)
            walk(data)

    for field in ('title', 'description', 'canonical'):
        counts = collections.Counter(v for v, _ in seen[field])
        for value, n in counts.items():
            if n > 1:
                where = ', '.join(p for v, p in seen[field] if v == value)
                errors.append('%d pages share the same %s: %s' % (n, field, where))

    for page, ref in refs:
        if ref not in ids:
            errors.append('%s: JSON-LD references @id %s, which nothing declares'
                          % (page, ref))

    if os.path.isfile('sitemap.xml'):
        listed = re.findall(r'<loc>(.*?)</loc>', open('sitemap.xml').read())
        if len(listed) != len(set(listed)):
            errors.append('sitemap.xml repeats a URL')
        on_disk = {DOMAIN + (p[:-len('index.html')] if p != 'index.html' else '')
                   for p in pages() if p.endswith('index.html')}
        for url in sorted(set(listed) - on_disk):
            errors.append('sitemap.xml lists %s, which has no page behind it' % url)
        for url in sorted(on_disk - set(listed)):
            errors.append('%s exists but is missing from sitemap.xml' % url)
    else:
        errors.append('no sitemap.xml')

    count = len(pages())
    if errors:
        print('audited %d pages\n' % count)
        for e in errors:
            print('  ' + e)
        print('\n%d problem(s).' % len(errors))
        return 1
    print('audited %d pages.\n\nMetadata, headings, structured data and the '
          'sitemap all hold.' % count)
    return 0


if __name__ == '__main__':
    sys.exit(main())
