#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stamps a content hash onto every stylesheet and script URL.

    python3 tools/stamp-assets.py            # stamp
    python3 tools/stamp-assets.py --check    # fail if any stamp is stale

WHY THIS EXISTS

On 2026-10-28 the live site showed the new logo squashed inside the old gold
disc. Nothing was wrong with the code: the host had served the NEW html
alongside a CACHED COPY OF THE OLD style.css, so the previous `.brand__mark`
rules -- border-radius, a gold gradient ground and a 52x52 box -- were still
being applied to the new <img>. Any CSS change can produce that pairing on a
caching host, and it is invisible in local testing because nothing local is
cached.

A URL carrying the file's own content hash cannot be answered from cache with
different bytes. Change the CSS and the URL changes with it, so the browser,
the CDN and LiteSpeed all have to fetch it. Change nothing and the URL is
stable, so the cache still does its job.

This is also why the stamp is a hash of the file rather than a hand-bumped
number: a number only works if someone remembers, and the failure it prevents
is silent.

RUN IT whenever assets/css/*.css or assets/js/*.js changes -- `--check` is a
pre-commit guard beside sync-partials.py, check-links.py and audit-seo.py.
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# only files the browser caches aggressively and that the HTML must stay in step with
ASSETS = ["assets/css/style.css", "assets/css/pages.css", "assets/js/main.js"]


def digest(rel):
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()[:8]


def main():
    check = "--check" in sys.argv
    stamps = {rel: digest(rel) for rel in ASSETS}
    names = {rel.rsplit("/", 1)[1]: v for rel, v in stamps.items()}
    pattern = re.compile(
        r'((?:href|src)=")((?:\.\./)*assets/(?:css|js)/(%s))(?:\?v=[0-9a-f]+)?(")'
        % "|".join(re.escape(n) for n in names))

    changed, stale = [], []
    for page in sorted(ROOT.rglob("*.html")):
        if "partials" in page.parts:
            continue              # partials are authored root-absolute and
            # rewritten by sync-partials.py; they carry no asset links today
        text = page.read_text(encoding="utf-8")
        new = pattern.sub(lambda m: "%s%s?v=%s%s" % (m.group(1), m.group(2),
                                                     names[m.group(3)], m.group(4)), text)
        if new != text:
            rel = page.relative_to(ROOT)
            (stale if check else changed).append(str(rel))
            if not check:
                page.write_text(new, encoding="utf-8")

    for rel, v in stamps.items():
        print("  %-24s v=%s" % (rel, v))
    if check:
        if stale:
            print("\n%d page(s) carry a stale or missing asset stamp:" % len(stale))
            for s in stale[:10]:
                print("   ", s)
            print("\nRun: python3 tools/stamp-assets.py")
            return 1
        print("\nEvery page requests the current CSS and JS by content hash.")
        return 0
    print("\n%d page(s) restamped." % len(changed) if changed
          else "\nAll pages were already current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
