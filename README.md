[![Release](https://img.shields.io/github/v/release/zawadzkim/cookiecutter-hydro)](https://pypi.org/project/cookiecutter-hydro/)
[![Build status](https://img.shields.io/github/actions/workflow/status/zawadzkim/cookiecutter-hydro/main.yml?branch=main)](https://github.com/zawadzkim/cookiecutter-hydro/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/cookiecutter-hydro)](https://pypi.org/project/cookiecutter-hydro/)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://zawadzkim.github.io/cookiecutter-hydro/)
[![License](https://img.shields.io/github/license/zawadzkim/cookiecutter-hydro)](https://img.shields.io/github/license/zawadzkim/cookiecutter-hydro)

## Main features

- [pixi](https://pixi.sh/latest/) for dependency and task management in generated projects
- Code quality with [ruff](https://github.com/astral-sh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/) and [prettier](https://prettier.io/)
- Containerization with [Docker](https://www.docker.com/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following two commands:

```bash
pip install cookiecutter-hydro
cchydro
```

Alternatively, install `cookiecutter` and directly pass the URL to this
Github repository to the `cookiecutter` command:

```bash
pip install cookiecutter
cookiecutter https://github.com/zawadzkim/cookiecutter-hydro.git
```

Create a repository on GitHub, and then run the following commands, replacing `<project-name>`, with the name that you gave the Github repository and
`<github_author_handle>` with your Github username.

```bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

Finally, install dependencies and run checks with

```bash
pixi install
pixi run all
```

You are now ready to start development on your project!

## Acknowledgements

This project is inspired by Cookiecutter Poetry and Cookiecutter Data Science, and is tailored for use in hydrological research.
