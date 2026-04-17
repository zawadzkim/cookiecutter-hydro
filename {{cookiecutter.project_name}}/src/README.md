# Source Modules

## Purpose

This directory contains modeling and analysis code used by scripts and notebooks.

## Layout

- foo.py: starter utility/example module

If your project combines multiple model sources, create one directory per
source under `src` (for example `modflow_local`, `pastas_runs`, or
`surface_water_model`) and keep each workflow isolated.

## Conventions

- keep functions pure where practical
- separate data IO from modeling logic
- prefer small modules with explicit interfaces

## Usage

Import source code from notebooks or scripts:

```python
from src.foo import foo
```
