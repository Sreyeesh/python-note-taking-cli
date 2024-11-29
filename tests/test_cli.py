import pytest
from click.testing import CliRunner
from app.cli import cli
from tests.helpers import reset_storage


def test_add_note_command():
    """Test the CLI add command."""
    reset_storage()
    runner = CliRunner()
    result = runner.invoke(cli, [
        "add",
        "Test Title",
        "Test Content",
        "--category",
        "Test Category",
        "--tags",
        "tag1,tag2",
    ])
    assert result.exit_code == 0
    assert "Note added: Test Title - Test Content (Category: Test Category, Tags: tag1, tag2)" in result.output


def test_list_notes_command_empty():
    """Test listing notes when no notes exist."""
    reset_storage()
    runner = CliRunner()
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "No notes found. Total pages: 0." in result.output


def test_list_notes_command_with_notes():
    """Test listing notes with existing notes."""
    reset_storage()
    runner = CliRunner()
    runner.invoke(cli, ["add", "Title 1", "Content 1", "--category", "General"])
    runner.invoke(cli, ["add", "Title 2", "Content 2", "--category", "Work"])
    result = runner.invoke(cli, ["list", "--page", "1", "--limit", "2"])
    assert result.exit_code == 0
    assert "1. Title: Title 1" in result.output


def test_delete_note_command():
    """Test the CLI delete command."""
    reset_storage()
    runner = CliRunner()
    runner.invoke(cli, ["add", "Delete Test", "Content for delete test"])
    result = runner.invoke(cli, ["delete", "Delete Test"])
    assert result.exit_code == 0
    assert "Note with title 'Delete Test' has been deleted." in result.output
