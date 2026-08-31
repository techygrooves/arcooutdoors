#!/usr/bin/env python3
"""Sync the canonical header/footer partials into every page.

This is an AUTHORING helper, not a build step. The committed HTML is complete
and static; the site deploys by copying the repository to any host, with this
script never running. Its only job is to stop twelve hand-maintained copies of
the navigation from drifting apart.

Usage
-----
    python3 tools/sync-partials.py            # rewrite pages in place
    python3 tools/sync-partials.py --check    # exit 1 if any page is stale

How it works
------------
`assets/partials/<name>.html` is the source of truth. Every page carries:

    <!-- @partial:header -->
    ...generated markup...
    <!-- @endpartial:header -->

Everything between the markers is replaced by the partial's body (its leading
HTML comment is stripped) and re-indented to match the opening marker.

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


def apply_partial(html: str, name: str, body: str) -> tuple[str, bool]:
    """Replace the marked region for `name`. Returns (html, changed)."""
    pattern = re.compile(
        r"([ \t]*)(<!--\s*@partial:%s\s*-->)(.*?)([ \t]*<!--\s*@endpartial:%s\s*-->)"
        % (re.escape(name), re.escape(name)),
        re.DOTALL,
    )
    match = pattern.search(html)
    if not match:
        return html, False

    indent = match.group(1)
    indented = "\n".join(
        (indent + line if line.strip() else "") for line in body.split("\n")
    )
    replacement = f"{indent}{match.group(2)}\n{indented}\n{indent}<!-- @endpartial:{name} -->"
    updated = html[: match.start()] + replacement + html[match.end():]
    return updated, updated != html


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
        html = original
        found_any = False

        for name, body in partials.items():
            html, _ = apply_partial(html, name, body)
            if f"@partial:{name}" in original:
                found_any = True

        rel = page.relative_to(ROOT)
        if not found_any:
            unmarked.append(rel)
        elif html != original:
            if check_only:
                stale.append(rel)
            else:
                page.write_text(html, encoding="utf-8")
                written.append(rel)

    for rel in unmarked:
        print(f"  skipped (no markers): {rel}")

    if check_only:
        for rel in stale:
            print(f"  STALE: {rel}")
        if stale:
            print(f"\n{len(stale)} page(s) out of sync. Run: python3 tools/sync-partials.py")
            return 1
        print("All pages are in sync with assets/partials/.")
        return 0

    for rel in written:
        print(f"  updated: {rel}")
    print(f"\n{len(written)} page(s) updated, {len(list(iter_pages())) - len(unmarked)} carry markers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
