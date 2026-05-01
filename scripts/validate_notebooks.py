"""
Validate all Jupyter notebooks in the repository.

This script checks that every .ipynb file is valid JSON and contains
at least the core Jupyter notebook fields.

Usage:
    python scripts/validate_notebooks.py
"""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_KEYS = {"cells", "metadata", "nbformat", "nbformat_minor"}


def validate_notebook(path: Path) -> None:
    """Validate a single notebook file."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc

    missing = REQUIRED_KEYS.difference(data.keys())
    if missing:
        raise ValueError(f"Notebook {path} is missing required keys: {sorted(missing)}")

    if not isinstance(data["cells"], list):
        raise ValueError(f"Notebook {path} has invalid 'cells' field")

    if not data["cells"]:
        raise ValueError(f"Notebook {path} has no cells")


def main() -> None:
    """Validate all notebooks under the notebooks directory."""
    notebook_paths = sorted(Path("notebooks").glob("*.ipynb"))

    if not notebook_paths:
        raise SystemExit("No notebooks found.")

    for path in notebook_paths:
        validate_notebook(path)
        print(f"OK: {path}")

    print(f"Validated {len(notebook_paths)} notebook(s).")


if __name__ == "__main__":
    main()
