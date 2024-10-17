[![Release](https://img.shields.io/github/v/release/fpgmaas/cookiecutter-poetry)](https://pypi.org/project/cookiecutter-poetry/)
[![Build status](https://img.shields.io/github/actions/workflow/status/fpgmaas/cookiecutter-poetry/main.yml?branch=main)](https://github.com/fpgmaas/cookiecutter-poetry/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/cookiecutter-poetry)](https://pypi.org/project/cookiecutter-poetry/)
[![License](https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry)](https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry)

## Main features

- [Poetry](https://python-poetry.org/) for dependency management
- [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), [deptry](https://github.com/fpgmaas/deptry/) and [prettier](https://prettier.io/)
- Containerization with [Docker](https://www.docker.com/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

An example of a repository generated with this package can be found [here](https://github.com/fpgmaas/cookiecutter-poetry-example).

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

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!

## Acknowledgements

This project is a fork of [Cookiecutter Poetry](https://github.com/fpgmaas/cookiecutter-poetry-example) and is partly inspired by [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science) project, but is tailored for use in hydrological research.
