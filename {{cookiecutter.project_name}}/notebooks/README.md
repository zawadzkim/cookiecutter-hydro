# Notebooks

## Purpose

Use notebooks for exploratory analysis, model checks, and visual summaries.
Keep notebooks small and focused.

## Naming convention

Notebook files must follow:

`[ISO date]-[analyst initials]-[2-4 word description].ipynb`

Example:

`2015-06-28-jw-initial-data-clean.ipynb`

Rules:

- date is generated in ISO 8601 format
- initials are 2-4 letters
- description is strict kebab-case with 2-4 words

Create notebooks manually following this naming convention to keep chronology,
authorship, and topic easy to scan in version control.

## Imports from src

The pixi environment sets `PYTHONPATH=.` so notebooks can import project code
directly when launched from the project root, for example:

```python
from src.foo import foo
```
