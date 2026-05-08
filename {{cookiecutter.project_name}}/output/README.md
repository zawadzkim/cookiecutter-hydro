# Output

## Purpose

Store generated outputs from scripts, models, and notebooks.

## Conventions

- do not hand-edit generated files
- include metadata/version tags in filenames when possible
- clean stale artifacts regularly

## Usage

`output` is exposed as a `pathlib.Path` via the project package:

```python
from {{cookiecutter.project_slug}}.paths import output

fig_path = output / "figures" / "summary.png"
```
