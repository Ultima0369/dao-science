"""Tests for project maintenance scripts."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_script(name: str) -> None:
    script = ROOT / "scripts" / name
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"{name} failed:\n{result.stdout}\n{result.stderr}"


def test_sync_docs() -> None:
    run_script("sync_docs.py")


def test_audit_links() -> None:
    run_script("audit_links.py")


def test_audit_nav_coverage() -> None:
    run_script("audit_nav_coverage.py")


def test_audit_math_delimiters() -> None:
    run_script("audit_math_delimiters.py")
