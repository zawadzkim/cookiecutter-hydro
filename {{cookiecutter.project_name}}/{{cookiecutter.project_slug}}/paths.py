"""Project root resolution.

Walks up from this file until a marker (``pyproject.toml`` or ``.git``)
is found, so ``ROOT`` stays valid regardless of cwd or where the package
moves to inside the repo.

    from {{cookiecutter.project_slug}}.paths import ROOT
    csv_file = ROOT / "data" / "processed" / "heads.csv"
    fig_file = ROOT / "output" / "figures" / "summary.png"
"""

from pathlib import Path

_MARKERS = ("pyproject.toml", ".git")


def _find_root(start: Path) -> Path:
    for path in (start, *start.parents):
        if any((path / marker).exists() for marker in _MARKERS):
            return path
    raise RuntimeError(f"Could not find project root above {start} (looked for {_MARKERS})")


ROOT: Path = _find_root(Path(__file__).resolve())

__all__ = ["ROOT"]
