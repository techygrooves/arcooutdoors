#!/usr/bin/env python3
"""Sync the canonical header/footer partials into every page, and rewrite
internal links so the site works wherever it is mounted.

This is an AUTHORING helper, not a build step. The committed HTML is complete
and static; the site deploys by copying the repository to any host, with this
script never running. It does two jobs:

1. **Partials.** `assets/partials/<name>.html` is the source of truth. Every
   page carries:

       <!-- @partial:header -->
       ...generated markup...
       <!-- @endpartial:header -->

   Everything between the markers is replaced by the partial's body and
   re-indented to match the opening marker.

2. **Portable paths.** Internal URLs are *authored* root-absolute (`/assets/…`,
   `/services/…`) because that is easy to write and easy to grep. This script
   rewrites them to depth-correct relative URLs (`../../assets/…`) so the site
   renders identically at a domain root (`https://www.arcooutdoors.com/`) and
   under a subpath (`https://user.github.io/arcooutdoors/`). Without this a
   project-page deployment loads no CSS, no JS and no images.

   The rewrite is idempotent: it only matches URLs with a leading slash, and a
   relative URL never has one. Absolute `https://` URLs, `#fragments`, `tel:`
   and `mailto:` are left alone, as are the canonical, Open Graph and JSON-LD
   URLs, which must keep pointing at the production domain.

Usage
-----
    python3 tools/sync-partials.py            # rewrite pages in place
    python3 tools/sync-partials.py --check    # exit 1 if any page is stale

Per-page differences never live in the markup. Use `<body data-page="...">` to
drive the current-page state; main.js reads it.

Dependencies: Python 3.8+ standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTIALS_DIR = ROOT / "assets" / "partials"

# Directories never scanned for pages.
SKIP_DIRS = {".git", "assets", "tools", "node_modules"}

LEADING_COMMENT = re.compile(r"\A\s*<!--.*?-->\s*", re.DOTALL)

# Attributes holding a single URL, and attributes holding a srcset-style list.
URL_ATTRS = ("href", "src", "action", "poster")
SET_ATTRS = ("srcset", "imagesrcset")


def load_partial(name: str) -> str:
    """Return a partial's body with its explanatory header comment removed."""
    text = (PARTIALS_DIR / f"{name}.html").read_text(encoding="utf-8")
    return LEADING_COMMENT.sub("", text).strip("\n")


def iter_pages():
    """Yield every .html page outside the skipped directories."""
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS:
            continue
        yield path


def prefix_for(page: Path) -> str:
    """Relative hop back to the site root from a page: '', '../', '../../'."""
    depth = len(page.relative_to(ROOT).parts) - 1
    return "../" * depth


def relativise(html: str, prefix: str) -> str:
    """Turn root-absolute internal URLs into ones relative to this page.

    Only `="/…"` is touched. Protocol-relative `//host/…` is skipped, since a
    leading double slash is an absolute URL, not a site-root path.
    """

    def one(url: str) -> str:
        if not url.startswith("/") or url.startswith("//"):
            return url
        out = prefix + url[1:]
        # The site root from a root-level page would otherwise be an empty href.
        return out or "./"

    def sub_url(m):
        return f'{m.group(1)}="{one(m.group(2))}"'

    def sub_set(m):
        parts = []
        for candidate in m.group(2).split(","):
            bits = candidate.strip().split()
            if not bits:
                continue
            bits[0] = one(bits[0])
            parts.append(" ".join(bits))
        return f'{m.group(1)}="{", ".join(parts)}"'

    html = re.sub(
        r'\b(%s)="(/[^"]*)"' % "|".join(URL_ATTRS), sub_url, html
    )
    html = re.sub(
        r'\b(%s)="([^"]*)"' % "|".join(SET_ATTRS), sub_set, html
    )
    return html


def apply_partial(html: str, name: str, body: str) -> str:
    """Replace the marked region for `name`, indented to match the marker."""
    pattern = re.compile(
        r"([ \t]*)(<!--\s*@partial:%s\s*-->)(.*?)([ \t]*<!--\s*@endpartial:%s\s*-->)"
        % (re.escape(name), re.escape(name)),
        re.DOTALL,
    )
    match = pattern.search(html)
    if not match:
        return html

    indent = match.group(1)
    indented = "\n".join(
        (indent + line if line.strip() else "") for line in body.split("\n")
    )
    replacement = (
        f"{indent}{match.group(2)}\n{indented}\n"
        f"{indent}<!-- @endpartial:{name} -->"
    )
    return html[: match.start()] + replacement + html[match.end():]


def render(page: Path, partials: dict) -> str:
    """The canonical content of a page: partials inserted, paths relativised."""
    html = page.read_text(encoding="utf-8")
    for name, body in partials.items():
        html = apply_partial(html, name, body)
    return relativise(html, prefix_for(page))


def main() -> int:
    check_only = "--check" in sys.argv

    if not PARTIALS_DIR.is_dir():
        print(f"error: {PARTIALS_DIR} not found", file=sys.stderr)
        return 2

    partials = {p.stem: load_partial(p.stem) for p in PARTIALS_DIR.glob("*.html")}
    if not partials:
        print("error: no partials found", file=sys.stderr)
        return 2

    stale, written, unmarked = [], [], []

    for page in iter_pages():
        original = page.read_text(encoding="utf-8")
        updated = render(page, partials)
        rel = page.relative_to(ROOT)

        if not any(f"@partial:{n}" in original for n in partials):
            unmarked.append(rel)
        elif updated != original:
            if check_only:
                stale.append(rel)
            else:
                page.write_text(updated, encoding="utf-8")
                written.append(rel)

    for rel in unmarked:
        print(f"  skipped (no markers): {rel}")

    if check_only:
        for rel in stale:
            print(f"  STALE: {rel}")
        if stale:
            print(f"\n{len(stale)} page(s) out of sync. Run: python3 tools/sync-partials.py")
            return 1
        print("All pages are in sync with assets/partials/, and paths are relative.")
        return 0

    for rel in written:
        print(f"  updated: {rel}")
    total = len(list(iter_pages())) - len(unmarked)
    print(f"\n{len(written)} page(s) updated, {total} carry markers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
