#!/usr/bin/env python3
"""Check cross-file consistency: badges, equation indexing, etc."""

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


def collect_md_files() -> list[Path]:
    files: set[Path] = set()
    skip_prefixes = (
        str(ROOT / "docs"),
        str(ROOT / ".github"),
    )
    allowlist = {
        "AUDIT_REPORT_2026-06-13.md",
        "AUDIT_REPORT_2026-06-14.md",
        "AUDIT_FIX_LOG_2026-06-13.md",
    }
    for d in CONTENT_DIRS:
        if d.is_dir():
            for p in d.rglob("*.md"):
                if str(p).startswith(skip_prefixes):
                    continue
                if p.name in allowlist:
                    continue
                files.add(p.resolve())
        elif d.suffix == ".md" and d.exists():
            files.add(d.resolve())
    return sorted(files)


def load_allowed_badges() -> set[str]:
    """Parse NOTATION.md for the evidence-badge table."""
    notation = (ROOT / "NOTATION.md").read_text(encoding="utf-8")
    allowed: set[str] = set()
    for line in notation.splitlines():
        m = re.search(r"\|\s*\*\*([A-Z])\*\*\s*\|\s*(\S+)", line)
        if m:
            allowed.add(m.group(1))
    if not allowed:
        raise RuntimeError("Could not parse allowed badges from NOTATION.md")
    return allowed


def check_badges(files: list[Path], allowed: set[str]) -> list[tuple[str, str, str]]:
    """Find badge uses that contain unknown letters or malformed syntax."""
    issues: list[tuple[str, str, str]] = []
    badge_group = re.compile(r"(?<!!)\[([A-Z](?:[+/][A-Z])*)\]")

    for p in files:
        text = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        for m in badge_group.finditer(text):
            group = m.group(1)
            for letter in re.split(r"[+/]", group):
                if letter not in allowed:
                    line = text[:m.start()].count(chr(10)) + 1
                    issues.append((rel, letter, f"unknown badge letter [{letter}] in [{group}] at line {line}"))
    return issues


def check_equation_index(files: list[Path]) -> list[tuple[str, str]]:
    """Warn about numbered equations that may be missing from GLOSSARY."""
    issues: list[tuple[str, str]] = []
    glossary = (ROOT / "GLOSSARY.md").read_text(encoding="utf-8")

    patterns = [
        re.compile(r"\\tag\{([^}]+)\}"),
        re.compile(r"\\quad\s*\((\d+[a-zA-Z]?)\)"),
        re.compile(r"\|\s*\$.+?\$\s*\|\s*\((\d+[a-zA-Z]?)\)\s*\|"),
    ]

    for p in files:
        text = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        seen: set[str] = set()
        for pat in patterns:
            for m in pat.finditer(text):
                num = m.group(1)
                if num and num not in seen:
                    seen.add(num)
                    if f"({num})" not in glossary:
                        issues.append((rel, f"equation ({num}) not found in GLOSSARY.md"))
    return issues


def main() -> int:
    files = collect_md_files()
    allowed = load_allowed_badges()
    badge_issues = check_badges(files, allowed)
    eq_issues = check_equation_index(files)

    exit_code = 0
    if badge_issues:
        print(f"BADGE CONSISTENCY ISSUES ({len(badge_issues)}):")
        for rel, badge, msg in badge_issues:
            print(f"  {rel}: [{badge}] -> {msg}")
        exit_code = 1
    else:
        print("All Markdown badges are consistent with NOTATION.md.")

    if eq_issues:
        print(f"\nEQUATION INDEX ISSUES ({len(eq_issues)}):")
        for rel, msg in eq_issues:
            print(f"  {rel}: {msg}")
        print("\nTip: add missing equations to GLOSSARY.md or suppress false positives.")
    else:
        print("\nNo unindexed numbered equations detected.")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
