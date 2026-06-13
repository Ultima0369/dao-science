#!/usr/bin/env python3
"""Check for potentially unmatched inline math delimiters."""

from pathlib import Path

CONTENT_DIRS = [
    Path("."),
    Path("0_motivation"),
    Path("1_first_principles"),
    Path("2_models"),
    Path("3_methodology"),
    Path("4_applications"),
    Path("verifiable_units"),
]

issues = []
for d in CONTENT_DIRS:
    if not d.exists():
        continue
    for p in d.rglob("*.md"):
        if "site/" in str(p) or "docs/" in str(p):
            continue
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        in_code = False
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            # Count single $ not part of $$ and not escaped
            count = 0
            j = 0
            while j < len(line):
                if line[j] == "\\" and j + 1 < len(line) and line[j + 1] == "$":
                    j += 2
                    continue
                if line[j] == "$":
                    if j + 1 < len(line) and line[j + 1] == "$":
                        j += 2
                        continue
                    count += 1
                j += 1
            if count % 2 != 0:
                issues.append((str(p), i, line.strip()[:100]))

if issues:
    print(f"Potential unmatched $ lines ({len(issues)}):")
    for f, i, line in issues[:30]:
        print(f"  {f}:{i}: {line}")
    raise SystemExit(1)
else:
    print("No obvious unmatched inline math delimiters.")
