from __future__ import annotations

import importlib
import os
from typing import Callable, cast


def _run_cookiecutter(template_dir: str) -> None:
    cookiecutter_module = importlib.import_module("cookiecutter.main")
    cookiecutter_fn = cast(Callable[[str], object], cookiecutter_module.cookiecutter)
    cookiecutter_fn(template_dir)


def main() -> int:
    cwd = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.join(cwd, ".."))
    _run_cookiecutter(package_dir)
    return 0
