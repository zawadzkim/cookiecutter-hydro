# Input Data

## Purpose

Store project datasets used by scripts and notebooks.

## Structure

- raw: unprocessed source files (CSV, rasters, etc.)
- processed: transformed data products used in analyses

## Versioning suggestions

For files in `processed`, use explicit, traceable names such as:

- `heads-monthly-v2026-04.csv`
- `aquifer-mask-utm32n-10m-v2.tif`
- `forcing-merged-qcpassed-v1.parquet`

Good patterns include date stamps, semantic versions, resolution/CRS tags,
and short processing qualifiers.

Both `raw` and `processed` are gitignored by default in this template.

## Usage

`raw` and `processed` are exposed as `pathlib.Path` objects:

```python
from input import processed

csv_file = processed / "heads-monthly-v2026-04.csv"
```
