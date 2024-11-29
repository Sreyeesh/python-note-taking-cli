import pytest
from click.testing import CliRunner
from app.cli import cli, get_note_app


@pytest.fixture
def runner():
    """Fixture to initialize the CLI runner."""
    return CliRunner()


def test_add_note_command(runner):
    """Test the CLI add command."""
    get_note_app(memory_only=True)
    result = runner.invoke(
        cli,
        ["add", "CLI Test Title", "CLI Test Content", "--category", "CLI Category", "--tags", "cli,testing"],
    )
    assert result.exit_code == 0
    assert "Note added: CLI Test Title - CLI Test Content (Category: CLI Category, Tags: cli, testing)" in result.output


def test_add_duplicate_note_command(runner):
    """Test adding a duplicate note via CLI."""
    get_note_app(memory_only=True)
    runner.invoke(cli, ["add", "Duplicate Title", "Original Content"])
    result = runner.invoke(cli, ["add", "Duplicate Title", "New Content"])
    assert result.exit_code == 0
    assert "Error: A note with the title 'Duplicate Title' already exists." in result.output


def test_list_notes_command(runner):
    """Test listing notes via CLI."""
    get_note_app(memory_only=True)
    runner.invoke(cli, ["add", "List Note 1", "List Content 1"])
    runner.invoke(cli, ["add", "List Note 2", "List Content 2"])
    result = runner.invoke(cli, ["list", "--page", "1", "--limit", "1"])
    assert result.exit_code == 0
    assert "Page 1 of 2" in result.output
    assert "List Note 1" in result.output


def test_delete_note_command(runner):
    """Test deleting a note via CLI."""
    get_note_app(memory_only=True)
    runner.invoke(cli, ["add", "Delete Me", "Delete Content"])
    result = runner.invoke(cli, ["delete", "Delete Me"])
    assert result.exit_code == 0
    assert "Note with title 'Delete Me' has been deleted." in result.output


def test_delete_nonexistent_note_command(runner):
    """Test deleting a nonexistent note via CLI."""
    get_note_app(memory_only=True)
    result = runner.invoke(cli, ["delete", "Nonexistent Note"])
    assert result.exit_code == 0
    assert "Note with title 'Nonexistent Note' not found." in result.output
