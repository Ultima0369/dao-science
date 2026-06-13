#!/usr/bin/env python3
"""Audit internal Markdown links for broken references."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIRS = [
    ROOT,
    ROOT / "0_motivation",
    ROOT / "1_first_principles",
    ROOT / "2_models",
    ROOT / "3_methodology",
    ROOT / "4_applications",
    ROOT / "verifiable_units",
]

md_files = []
for d in CONTENT_DIRS:
    if d.is_dir():
        md_files.extend(d.rglob("*.md"))
    elif d.suffix == ".md" and d.exists():
        md_files.append(d)

existing = {str(p.resolve()).replace("\\", "/") for p in md_files}

broken = []
for p in md_files:
    text = p.read_text(encoding="utf-8")
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
        link = m.group(2)
        if link.startswith("http") or link.startswith("#") or link.startswith("mailto"):
            continue
        if link.endswith(".md"):
            target = (p.parent / link).resolve()
            target_str = str(target).replace("\\", "/")
            if target_str not in existing:
                broken.append((str(p).replace("\\", "/"), link, target_str))

if broken:
    print(f"BROKEN INTERNAL LINKS ({len(broken)}):")
    for src, link, target in broken:
        print(f"  {src} -> {link} (resolved: {target})")
    raise SystemExit(1)
else:
    print("No broken internal .md links found.")
