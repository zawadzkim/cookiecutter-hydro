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
- `src/{{cookiecutter.project_slug}}`: project package (editable-installed)

If you work with multiple model sources in one project, create dedicated
submodules under `src/{{cookiecutter.project_slug}}/` (for example
`modflow_local`, `pastas_runs`, `custom_model`) so code and assumptions
stay separated.

## Testing

This template includes one example pytest (`tests/test_foo.py`) for the starter
`foo` function. Use it as a pattern when adding tests for your own models,
data transforms, and calibration workflows.

Run tests with:

```bash
pixi run test
```
