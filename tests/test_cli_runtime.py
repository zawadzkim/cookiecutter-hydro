from __future__ import annotations

from pathlib import Path

import pytest

from cookiecutter_hydro import cli


def test_main_invokes_cookiecutter_with_template_dir(monkeypatch):
    captured: dict[str, object] = {}

    class FakeCookiecutterModule:
        @staticmethod
        def cookiecutter(template_dir: str) -> None:
            captured["template_dir"] = template_dir

    monkeypatch.setattr(cli.importlib, "import_module", lambda _: FakeCookiecutterModule)

    exit_code = cli.main([])

    expected_package_dir = str(Path(cli.__file__).resolve().parent.parent)
    assert exit_code == 0
    assert captured["template_dir"] == expected_package_dir


def test_main_propagates_cookiecutter_errors(monkeypatch):
    class CookiecutterError(RuntimeError):
        pass

    class FakeCookiecutterModule:
        @staticmethod
        def cookiecutter(template_dir: str) -> None:
            raise CookiecutterError

    monkeypatch.setattr(cli.importlib, "import_module", lambda _: FakeCookiecutterModule)

    with pytest.raises(CookiecutterError):
        cli.main([])


def test_main_help_exits_without_baking(monkeypatch):
    called = {"ran": False}

    def fake_run_cookiecutter(template_dir: str) -> None:
        called["ran"] = True

    monkeypatch.setattr(cli, "_run_cookiecutter", fake_run_cookiecutter)

    with pytest.raises(SystemExit) as exc:
        cli.main(["--help"])

    assert exc.value.code == 0
    assert called["ran"] is False
