# Task Runner (pixi)

Generated repositories use `pixi` tasks instead of a Makefile.

Common tasks:

```bash
pixi install
pixi run lint
pixi run type-check
pixi run test
pixi run all
```

The `all` task is the quality gate and runs linting, typing, and tests.

If `dockerfile` is enabled, additional container workflow tasks are available:

```bash
pixi run img
pixi run drun
pixi run dnb
pixi run dtest
```
