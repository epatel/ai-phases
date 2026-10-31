#!/usr/bin/env python3
"""Check that every image and local link in the post files resolves.

Usage: python3 scripts/check_post.py [FILE ...]   (defaults to blog-post.md blog-post.html)
Exits 1 if anything is missing. External links are listed, not fetched.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = sys.argv[1:] or ["blog-post.md", "blog-post.html"]

MD_REF = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")
HTML_REF = re.compile(r'(?:src|href)="([^"]+)"')


def refs(path):
    text = path.read_text()
    pattern = HTML_REF if path.suffix == ".html" else MD_REF
    return pattern.findall(text)


missing, external = [], set()
for name in FILES:
    path = ROOT / name
    for ref in refs(path):
        if ref.startswith(("http://", "https://")):
            external.add(ref)
        elif ref.startswith(("#", "mailto:")):
            continue
        elif not (path.parent / ref.split("#")[0]).exists():
            missing.append(f"{name}: {ref}")

for line in missing:
    print(f"MISSING {line}")
for url in sorted(external):
    print(f"external {url}")
print(f"{len(missing)} missing, {len(external)} external link(s) not fetched")
sys.exit(1 if missing else 0)
