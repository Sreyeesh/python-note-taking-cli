# tests/test_cli.py

import pytest
from click.testing import CliRunner
from app.cli import cli


@pytest.fixture
def runner():
    """Fixture to provide a CLI runner for testing."""
    return CliRunner()


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

def test_search_command(runner):
    runner.invoke(cli, ["add", "Grocery List", "Buy milk and eggs", "--category", "Personal"])
    result = runner.invoke(cli, ["search", "milk"])
    assert result.exit_code == 0
    assert "Grocery List" in result.output

def test_search_command_with_category(runner):
    runner.invoke(cli, ["add", "Grocery List", "Buy milk and eggs", "--category", "Personal"])
    result = runner.invoke(cli, ["search", "milk", "--category", "Personal"])
    assert result.exit_code == 0
    assert "Personal" in result.output
