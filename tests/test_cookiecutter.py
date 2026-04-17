from __future__ import annotations

import os
import shlex
import shutil
import subprocess

import pytest

from tests.utils import run_within_dir


def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_name": "my-project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.project_path.is_dir()
    assert not (result.project_path / ".github").exists()
    assert not (result.project_path / "tox.ini").exists()


def test_bake_project_in_current_directory(cookies, tmp_path):
    project_home = tmp_path / "my-project"
    project_home.mkdir()

    with run_within_dir(project_home):
        result = cookies.bake(
            extra_context={
                "project_name": "my-project",
                "project_home": "current-directory",
            }
        )

    assert result.exit_code == 0
    assert result.exception is None
    # In current-directory mode, files are moved one level up from the
    # generated folder and the generated folder is removed.
    assert (result.project_path.parent / "pixi.toml").is_file()
    assert (result.project_path.parent / "README.md").is_file()
    assert not result.project_path.exists()


def test_using_pytest(cookies, tmp_path):
    if shutil.which("pixi") is None:
        pytest.skip("pixi is required to run generated-project smoke tests")

    with run_within_dir(tmp_path):
        result = cookies.bake()

        # Assert that project was created.
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "example-project"
        assert result.project_path.is_dir()

        # Install the pixi environment and run tests.
        with run_within_dir(str(result.project_path)):
            assert not os.path.isfile(f"{result.project_path}/Makefile")
            assert subprocess.check_call(shlex.split("pixi install")) == 0
            assert subprocess.check_call(shlex.split("pixi run test")) == 0


def test_devcontainer(cookies, tmp_path):
    """Test that the devcontainer files are created when devcontainer=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_not_devcontainer(cookies, tmp_path):
    """Test that the devcontainer files are not created when devcontainer=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert not os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_dockerfile(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/Dockerfile")


def test_not_dockerfile(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/Dockerfile")
