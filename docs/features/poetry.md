# Dependency Management

Generated repositories use [pixi](https://pixi.sh/latest/) for dependency management and task execution.

Install and lock dependencies with:

```bash
pixi install
```

Run project commands through pixi tasks:

```bash
pixi run test
pixi run type-check
pixi run lint
```

To add Python package dependencies, edit `pixi.toml` under `[pypi-dependencies]`.

The root `cookiecutter-hydro` repository itself remains Poetry-managed.
