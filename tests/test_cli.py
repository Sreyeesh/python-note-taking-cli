from click.testing import CliRunner
from app.cli import cli, get_note_app

def test_list_command_with_notes():
    """Test the CLI list command with existing notes."""
    runner = CliRunner()

    # Initialize the NoteApp instance in memory-only mode
    get_note_app(memory_only=True)

    # Add notes using the CLI
    runner.invoke(cli, ["add", "Title 1", "Content 1"])
    runner.invoke(cli, ["add", "Title 2", "Content 2"])

    # List notes with pagination
    result = runner.invoke(cli, ["list", "--page", "1", "--limit", "1"])
    assert result.exit_code == 0
    assert "Title 1" in result.output
    assert "Page 1 of 2" in result.output

def test_list_command_empty():
    """Test the CLI list command when no notes exist."""
    runner = CliRunner()

    # Initialize the NoteApp instance in memory-only mode
    get_note_app(memory_only=True)

    # Invoke the list command
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "No notes found" in result.output

def test_add_note_command():
    """Test the CLI add command."""
    runner = CliRunner()

    # Initialize the NoteApp instance in memory-only mode
    get_note_app(memory_only=True)

    # Add a note and verify the output
    result = runner.invoke(
        cli,
        ["add", "Test Title", "Test Content", "--category", "Test Category", "--tags", "tag1,tag2"]
    )
    assert result.exit_code == 0
    assert "Note added: Test Title - Test Content (Category: Test Category, Tags: tag1, tag2)" in result.output
