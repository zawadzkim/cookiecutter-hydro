# Scripts

Utility functions and small task scripts that support the project's
analyses and notebooks.

Because this is a subpackage of `{{cookiecutter.project_slug}}`, anything
you drop here is importable from anywhere once the package is
editable-installed:

```python
from {{cookiecutter.project_slug}}.scripts.preprocess import clean_heads
```

Keep modules small and focused. If a module grows beyond utilities into a
distinct concern (modeling, plotting, IO), promote it to a top-level
submodule of `{{cookiecutter.project_slug}}/`.
