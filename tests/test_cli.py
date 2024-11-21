# tests/test_cli.py

from click.testing import CliRunner
from app.cli import cli

def test_add_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "CLI Title", "CLI Content", "--category", "CLI Category"])
    assert result.exit_code == 0
    assert "Note added: CLI Title" in result.output

def test_list_command():
    runner = CliRunner()
    runner.invoke(cli, ["add", "CLI Title", "CLI Content"])
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "CLI Title" in result.output
