# Linting and code quality

Code can be linted and quality-checked with the command

```bash
pixi run all
```

This command will run the following tools:

## ruff

[ruff](https://github.com/astral-sh/ruff) is used to lint and format the code.

The template does not require a dedicated ruff config file by default; add one
(`ruff.toml` or `.ruff.toml`) if you want custom rules.

# mypy

[mypy](https://mypy.readthedocs.io/en/stable/) is used for static type
checking. Add a `mypy.ini` (or equivalent) if you want custom settings.

The `pixi run lint` task runs ruff directly on
`src`.

# Prettier

[Prettier](https://prettier.io/) is used to format the markdown documentation, along with any json and yaml files.
Its options can be configured in the included `.editorconfig` file or in greater detail by adding a `.prettierrc` file ([See Docs](https://prettier.io/docs/en/configuration)).

```yaml
[*]
max_line_length = 120

[*.json]
indent_style = space
indent_size = 4
```
