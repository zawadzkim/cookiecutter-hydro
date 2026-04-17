from __future__ import annotations

import argparse
import importlib
import os
from typing import Callable, cast


def _run_cookiecutter(template_dir: str) -> None:
    cookiecutter_module = importlib.import_module("cookiecutter.main")
    cookiecutter_fn = cast(Callable[[str], object], cookiecutter_module.cookiecutter)
    cookiecutter_fn(template_dir)


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cchydro",
        description="Generate a project from the local cookiecutter-hydro template.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    _parse_args(argv)
    cwd = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.join(cwd, ".."))
    _run_cookiecutter(package_dir)
    return 0
