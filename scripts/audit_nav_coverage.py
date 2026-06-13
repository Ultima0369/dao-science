#!/usr/bin/env python3
"""Check that all Markdown files in content dirs are referenced in mkdocs nav."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

with open(ROOT / "mkdocs.yml", encoding="utf-8") as f:
    text = f.read()

nav_paths = set()
for line in text.splitlines():
    m = re.search(r":\s+(\S+\.md)$", line)
    if m:
        nav_paths.add(m.group(1))

content_dirs = [
    "0_motivation",
    "1_first_principles",
    "2_models",
    "3_methodology",
    "4_applications",
    "verifiable_units",
]

def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")

all_files = [rel(p) for p in ROOT.glob("*.md")]
for d in content_dirs:
    all_files.extend(rel(p) for p in (ROOT / d).rglob("*.md"))

ALLOWLIST = {
    "AUDIT_REPORT_2026-06-13.md",
    "CODE_OF_CONDUCT.md",
    "对话记录.md",
    "对话记录2.md",
    "认知过程正在进行时_书籍.md",
}

unreferenced = (set(all_files) - nav_paths) - ALLOWLIST
if unreferenced:
    print("Unreferenced .md files:")
    for f in sorted(unreferenced):
        print(f"  - {f}")
    raise SystemExit(1)
else:
    print("All .md files in content dirs are referenced in nav.")
