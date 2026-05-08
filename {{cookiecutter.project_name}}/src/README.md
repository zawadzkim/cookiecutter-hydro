# Source Modules

## Purpose

This directory contains the project package — modeling and analysis code
used by scripts and notebooks.

## Layout

The package lives at `src/{{cookiecutter.project_slug}}/` and is installed in
editable mode by pixi (see `pyproject.toml` and `pixi.toml`).

- `paths.py`: `pathlib.Path` handles for `data/raw`, `data/processed`, and
  `output`.

If your project combines multiple model sources, add submodules under
`src/{{cookiecutter.project_slug}}/` (for example `modflow_local`,
`pastas_runs`, `surface_water_model`) and keep each workflow isolated.

## Conventions

- keep functions pure where practical
- separate data IO from modeling logic
- prefer small modules with explicit interfaces

## Usage

Because the package is editable-installed, imports work from anywhere:

```python
from {{cookiecutter.project_slug}}.paths import processed
from {{cookiecutter.project_slug}} import some_module
```
