from __future__ import annotations

import os
import subprocess


def main() -> int:
    cwd = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.join(cwd, ".."))
    return subprocess.call(["cookiecutter", package_dir])
