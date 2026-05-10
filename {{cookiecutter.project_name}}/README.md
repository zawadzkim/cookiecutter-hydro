# {{cookiecutter.project_name}}

[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>

## Quickstart

```bash
pixi install
pixi run all
```

## Project layout

- `data/raw`: raw, unprocessed data files (gitignored)
- `data/processed`: transformed datasets ready for analysis (gitignored)
- `notebooks`: exploratory notebooks
- `output`: generated artifacts and figures
- `docs`: project notes and methodological documentation
- `{{cookiecutter.project_slug}}/`: project package (editable-installed). Exposes
  `ROOT` (a `pathlib.Path` to the repo root) via `paths.py`. Add submodules
  here for reusable code (e.g. `io.py`, `models/`, `viz.py`).
- `{{cookiecutter.project_slug}}/scripts/`: utility functions and small task
  scripts, importable from notebooks and other code.

If you work with multiple model sources in one project, create dedicated
submodules under `{{cookiecutter.project_slug}}/` (for example
`modflow_local`, `pastas_runs`, `custom_model`) so code and assumptions
stay separated.

## Paths in notebooks and scripts

Because the package is editable-installed, you can compose paths relative
to the repo root regardless of cwd:

```python
from {{cookiecutter.project_slug}}.paths import ROOT

raw = ROOT / "data" / "raw"
processed = ROOT / "data" / "processed"
output = ROOT / "output"
```

## Testing

Add tests under `tests/` and run them with:

```bash
pixi run test
```
