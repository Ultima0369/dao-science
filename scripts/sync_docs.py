#!/usr/bin/env python3
"""Sync root Markdown content into docs/ for MkDocs builds.

Project Dao.Science keeps source Markdown files at the repository root and in
topic directories (0_motivation/, 1_first_principles/, ...). MkDocs requires all
source files to live under a single docs_dir. This script mirrors those files
into docs/ before building.
"""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

CONTENT_DIRS = [
    "0_motivation",
    "1_first_principles",
    "2_models",
    "3_methodology",
    "4_applications",
    "verifiable_units",
]
TOP_FILES = [
    "BEFORE_YOU_READ_ANYTHING.md",
    "README.md",
    "POSITIONING.md",
    "FINAL_VISION.md",
    "GLOSSARY.md",
    "NOTATION.md",
    "TRANSLATION.md",
    "CONTRIBUTING.md",
    "CLAIMS.md",
    "认知过程正在进行时_书籍.md",
    "对话记录.md",
    "对话记录2.md",
]

# Files/directories that should not be mirrored even if listed above.
EXCLUDE_DIRS = {".git", "site", "docs", "scripts", "paper"}


def _remove(path: Path) -> None:
    if path.is_symlink():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def main() -> None:
    DOCS.mkdir(exist_ok=True)

    # Mirror content directories.
    for name in CONTENT_DIRS:
        src = ROOT / name
        dst = DOCS / name
        if not src.exists():
            print(f"Warning: source directory not found: {src}")
            continue
        _remove(dst)
        shutil.copytree(src, dst)

    # Mirror top-level pages.
    for name in TOP_FILES:
        src = ROOT / name
        dst = DOCS / name
        if not src.exists():
            print(f"Warning: source file not found: {src}")
            continue
        # If root and docs copies are hard-linked, they already share content.
        try:
            if src.samefile(dst):
                continue
        except OSError:
            pass
        shutil.copy2(src, dst)

    # Mirror top-level English translations if present.
    for name in TOP_FILES:
        en_name = name.replace(".md", ".en.md")
        src = ROOT / en_name
        dst = DOCS / en_name
        if not src.exists():
            continue
        try:
            if src.samefile(dst):
                continue
        except OSError:
            pass
        shutil.copy2(src, dst)

    print("docs/ mirror synced from repository root.")


if __name__ == "__main__":
    main()
