#!/usr/bin/env python
from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

PROJECT_DIRECTORY = Path(os.path.realpath(os.path.curdir))


def remove_file(filepath: str) -> None:
    os.remove(PROJECT_DIRECTORY / filepath)


def remove_dir(filepath: str) -> None:
    shutil.rmtree(PROJECT_DIRECTORY / filepath)


def move_project_to_parent() -> None:
    parent_directory = PROJECT_DIRECTORY.parent
    conflicts = [path.name for path in PROJECT_DIRECTORY.iterdir() if (parent_directory / path.name).exists()]

    if conflicts:
        print(
            "ERROR: Cannot use 'current-directory' because files already exist in the target directory: "
            + ", ".join(sorted(conflicts))
        )
        sys.exit(1)

    for path in PROJECT_DIRECTORY.iterdir():
        shutil.move(str(path), str(parent_directory / path.name))

    os.chdir(parent_directory)
    PROJECT_DIRECTORY.rmdir()


if __name__ == "__main__":
    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    if "{{cookiecutter.project_home}}" == "current-directory":
        move_project_to_parent()
