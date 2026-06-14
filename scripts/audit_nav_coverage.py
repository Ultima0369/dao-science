#!/usr/bin/env python3
"""Check that all Markdown files in content dirs are referenced in mkdocs nav."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

with open(ROOT / "mkdocs.yml", encoding="utf-8") as mkdocs_file:
    text = mkdocs_file.read()

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

all_files = [rel(p) for p in ROOT.glob("*.md") if not p.name.endswith(".en.md")]
for d in content_dirs:
    all_files.extend(rel(p) for p in (ROOT / d).rglob("*.md") if not p.name.endswith(".en.md"))

ALLOWLIST = {
    "AUDIT_REPORT_2026-06-13.md",
    "AUDIT_FIX_LOG_2026-06-13.md",
    "AUDIT_REPORT_2026-06-14.md",
    "AUDIT_REPORT_2026-06-14_工程化审计.md",
    "AUDIT_REPORT_2026-06-14_SELF_REFLEXIVE.md",
    "CODE_OF_CONDUCT.md",
}

unreferenced = (set(all_files) - nav_paths) - ALLOWLIST
if unreferenced:
    print("Unreferenced .md files:")
    for path in sorted(unreferenced):
        print(f"  - {path}")
    raise SystemExit(1)
else:
    print("All .md files in content dirs are referenced in nav.")
