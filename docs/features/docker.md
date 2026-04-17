# Containerization with Docker

If `dockerfile` is set to `"y"`, a simple `Dockerfile` is added to the
repository. The Dockerfile installs pixi, sets up the environment and runs
`foo.py` when run.

The container image now bakes only the runtime dependencies and expects project
files (`src`, `tests`, `notebooks`, `input`) to be mounted as a volume at
runtime. This better simulates running the same code/data snapshot in another
environment (for example, HPC execution contexts).

The generated `pixi.toml` also includes container workflow tasks to simulate
running model workflows in a reproducible environment (for example, to mimic
HPC-style execution):

```bash
pixi run img
pixi run drun
pixi run dnb
pixi run dtest
```

`dnb` executes `notebooks/workflow.ipynb` with
`jupyter nbconvert --execute` and writes `workflow-executed.ipynb`.
Adjust the notebook path to match your project notebooks.

The docker image can be built with

```bash
docker build . -t my-docker-image
```

It can then be run against your project directory with a mounted volume, for
example:

```bash
docker run --rm -v "$PWD":/workspace -w /workspace my-docker-image
```

Or run it in interactive mode with

```
docker run --rm -it -v "$PWD":/workspace -w /workspace --entrypoint bash my-docker-image
```
