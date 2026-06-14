"""Compatibility shim for running simulations directly from the repository.

If the `dao_science` package is not installed (e.g., when executing a script
standalone without `pip install -e .`), this module adds the repository's
`src/` directory to `sys.path` so that the formalization stubs remain importable.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import dao_science  # noqa: F401
except ImportError:  # pragma: no cover
    src_dir = Path(__file__).resolve().parent.parent / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))
