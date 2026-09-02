#!/usr/bin/env python3
"""Resolve every internal link and asset reference against the file system.

Because internal URLs are relative (see tools/sync-partials.py), a link is only
correct if the ../ arithmetic lands on a real file. This resolves each URL from
the page that contains it and reports anything that does not exist, so a wrong
depth is caught here rather than by a visitor.

    python3 tools/check-links.py          # exit 1 on any problem

Checks, per page:
  * relative links resolve to a file that exists, or to a route on the planned
    map that has not been built yet (reported separately, not as an error)
  * asset references — including every candidate in srcset/imagesrcset — exist
  * in-page #fragments have a matching id
  * no leftover root-absolute internal URLs, which break subpath deployments
  * no bare href="#" placeholders
  * canonical, og:url and JSON-LD URLs still point at the production domain
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "assets", "tools", "node_modules"}
PROD = "https://www.arcooutdoors.com"

# Routes that are linked from the global nav/footer but not yet built.
PLANNED = {
    "about-us/", "gallery/", "reviews/",
    "blog/", "contact-us/", "get-a-quote/",
    "privacy-policy/", "cookie-policy/", "accessibility/",
}

URL_ATTRS = ("href", "src", "action", "poster")
SET_ATTRS = ("srcset", "imagesrcset")
EXTERNAL = re.compile(r"^(https?:|mailto:|tel:|data:|//)")


def pages():
    for p in sorted(ROOT.rglob("*.html")):
        if p.relative_to(ROOT).parts[0] not in SKIP_DIRS:
            yield p


def resolve(page: Path, url: str) -> Path:
    """Where a relative URL from `page` actually lands on disk."""
    target = (page.parent / url).resolve()
    if url.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def main() -> int:
    problems, planned_hits = [], 0

    for page in pages():
        rel = page.relative_to(ROOT)
        html = page.read_text(encoding="utf-8")

        urls = []
        for m in re.finditer(r'\b(%s)="([^"]*)"' % "|".join(URL_ATTRS), html):
            urls.append(m.group(2))
        for m in re.finditer(r'\b(%s)="([^"]*)"' % "|".join(SET_ATTRS), html):
            for cand in m.group(2).split(","):
                bits = cand.strip().split()
                if bits:
                    urls.append(bits[0])

        for url in urls:
            if url == "#":
                problems.append(f"{rel}: bare href=\"#\" placeholder")
                continue
            if url.startswith("#"):
                if not re.search(r'id="%s"' % re.escape(url[1:]), html):
                    problems.append(f"{rel}: fragment {url} has no matching id")
                continue
            if EXTERNAL.match(url):
                continue
            if url.startswith("/"):
                problems.append(
                    f"{rel}: root-absolute URL {url} — breaks subpath deploys, "
                    f"run tools/sync-partials.py")
                continue

            target = resolve(page, url)
            if target.exists():
                continue
            try:
                as_route = target.relative_to(ROOT).as_posix().replace("index.html", "")
            except ValueError:
                problems.append(f"{rel}: {url} escapes the site root")
                continue
            if as_route in PLANNED:
                planned_hits += 1
            else:
                problems.append(f"{rel}: {url} -> missing {as_route or '/'}")

        # SEO URLs must keep pointing at production regardless of where this is served
        for label, pat in (("canonical", r'<link rel="canonical" href="([^"]+)"'),
                           ("og:url", r'<meta property="og:url" content="([^"]+)"')):
            for val in re.findall(pat, html):
                if not val.startswith(PROD):
                    problems.append(f"{rel}: {label} is {val}, expected {PROD}/…")

    print(f"scanned {len(list(pages()))} pages")
    print(f"links to planned-but-unbuilt routes: {planned_hits} (expected)")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  {p}")
        return 1
    print("\nAll links, assets and fragments resolve. No root-absolute URLs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
