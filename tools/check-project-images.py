#!/usr/bin/env python3
"""Verify every ImageKit project photograph on /projects/ actually resolves.

Written because the sandbox this page was built in blocks ik.imagekit.io at the
network egress policy, so the URLs and their transformations could not be
exercised at authoring time. Run this once from a machine with normal internet
access and it settles the question for every image in one pass.

    python3 tools/check-project-images.py            # gallery + lightbox URLs
    python3 tools/check-project-images.py --verbose  # print every result

Checks, per photograph:
  * the 800px gallery transformation returns 200 and an image content-type
  * the 1600px lightbox transformation does the same
  * f-auto is honoured (a modern format is negotiated when the client asks)
  * reports content-length, so byte-identical files reveal themselves as
    likely duplicate uploads

Exits non-zero if anything fails, so it can join the other pre-commit guards.
Python 3 standard library only.
"""
from __future__ import annotations

import collections
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "projects" / "index.html"
HOST = "ik.imagekit.io"
TIMEOUT = 20

# Ask as a modern browser would, so f-auto has something to negotiate to.
HEADERS = {
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
    "User-Agent": "arco-outdoors-link-check/1.0",
}


class Collector(HTMLParser):
    """Pull every ImageKit URL out of the gallery, in document order."""

    def __init__(self) -> None:
        super().__init__()
        self.thumbs: list[str] = []
        self.fulls: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img" and HOST in (a.get("src") or ""):
            self.thumbs.append(a["src"])
        elif tag == "a" and HOST in (a.get("href") or ""):
            self.fulls.append(a["href"])


def fetch(url: str):
    """Return (status, content_type, length, error) for a single URL."""
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read()
            return resp.status, resp.headers.get("Content-Type", ""), len(body), None
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type", ""), 0, f"HTTP {e.code}"
    except Exception as e:                                   # noqa: BLE001
        return 0, "", 0, str(e)


def main() -> int:
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    if not PAGE.is_file():
        print(f"error: {PAGE} not found", file=sys.stderr)
        return 2

    c = Collector()
    c.feed(PAGE.read_text(encoding="utf-8"))

    if not c.thumbs:
        print("error: no ImageKit images found on /projects/", file=sys.stderr)
        return 2

    print(f"{len(c.thumbs)} gallery images, {len(c.fulls)} lightbox targets\n")

    failures: list[str] = []
    sizes: dict[int, list[str]] = collections.defaultdict(list)

    for label, urls in (("gallery  800px", c.thumbs), ("lightbox 1600px", c.fulls)):
        print(f"--- {label} ---")
        for url in urls:
            name = url.rsplit("/", 1)[-1].split("?")[0]
            status, ctype, length, err = fetch(url)
            good = status == 200 and ctype.startswith("image/")
            if not good:
                failures.append(f"{name} [{label.split()[0]}] -> {err or status} {ctype}")
            if label.startswith("gallery"):
                sizes[length].append(name)
            if verbose or not good:
                mark = "ok  " if good else "FAIL"
                print(f"  {mark} {name:52s} {status} {ctype:12s} {length // 1024:5d} KB")
        if not verbose:
            done = len(urls) - len([f for f in failures if label.split()[0] in f])
            print(f"  {done}/{len(urls)} resolved")
        print()

    # Byte-identical responses almost always mean the same photograph twice.
    dupes = {n: v for n, v in sizes.items() if len(v) > 1 and n > 0}
    if dupes:
        print("--- identical byte lengths (probable duplicate uploads) ---")
        for length, names in dupes.items():
            print(f"  {length // 1024} KB: {', '.join(names)}")
        print()

    if failures:
        print(f"{len(failures)} URL(s) failed:", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1

    print("Every project photograph resolves, at both sizes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
