"""Path handles for project data and output directories.

Resolves paths relative to the repo root, regardless of cwd. Works once the
package is editable-installed (see pyproject.toml + pixi.toml).

    from {{cookiecutter.project_slug}}.paths import processed, output
    csv_file = processed / "heads-monthly-v2026-04.csv"
    fig_file = output / "figures" / "summary.png"
"""

from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]

raw: Path = _ROOT / "data" / "raw"
processed: Path = _ROOT / "data" / "processed"
output: Path = _ROOT / "output"

__all__ = ["raw", "processed", "output"]
