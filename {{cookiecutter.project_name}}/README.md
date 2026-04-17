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

- `input/raw`: raw, unprocessed data files (gitignored)
- `input/processed`: transformed datasets ready for analysis (gitignored)
- `notebooks`: exploratory notebooks
- `output`: generated artifacts and figures
- `docs`: project notes and methodological documentation
- `src`: model and workflow code

If you work with multiple model sources in one project, create dedicated
subdirectories under `src` (for example
`src/modflow_local`, `src/pastas_runs`, `src/custom_model`) so code and
assumptions stay separated.

## Testing

This template includes one example pytest (`tests/test_foo.py`) for the starter
`foo` function. Use it as a pattern when adding tests for your own models,
data transforms, and calibration workflows.

Run tests with:

```bash
pixi run test
```
