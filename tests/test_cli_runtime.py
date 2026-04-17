from __future__ import annotations

from pathlib import Path

from cookiecutter_hydro import cli


def test_main_invokes_cookiecutter_with_template_dir(monkeypatch):
    captured: dict[str, object] = {}

    def fake_call(args: list[str]) -> int:
        captured["args"] = args
        return 0

    monkeypatch.setattr(cli.subprocess, "call", fake_call)

    exit_code = cli.main()

    expected_package_dir = str(Path(cli.__file__).resolve().parent.parent)
    assert exit_code == 0
    assert captured["args"] == ["cookiecutter", expected_package_dir]


def test_main_returns_subprocess_exit_code(monkeypatch):
    def fake_call(args: list[str]) -> int:  # noqa: ARG001
        return 2

    monkeypatch.setattr(cli.subprocess, "call", fake_call)

    assert cli.main() == 2
