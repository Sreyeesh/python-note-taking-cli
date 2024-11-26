import pytest
from click.testing import CliRunner
from app.cli import cli
from app.note_app import NoteApp

@pytest.fixture
def runner():
    """Fixture to create a CLI runner for testing."""
    return CliRunner()

@pytest.fixture
def clean_environment(monkeypatch):
    """Fixture to create an isolated in-memory NoteApp instance for testing."""
    def mock_note_app():
        return NoteApp(use_memory=True)
    monkeypatch.setattr("app.cli.note_app", mock_note_app())

def test_list_command(runner, clean_environment):
    """Test the list command."""
    runner.invoke(cli, ["add", "Note 1", "Content 1", "--category", "Personal"])
    runner.invoke(cli, ["add", "Note 2", "Content 2", "--category", "Work"])
    result = runner.invoke(cli, ["list", "--page", "1", "--limit", "2"])
    assert result.exit_code == 0
    assert "Note 1" in result.output
    assert "Note 2" in result.output

def test_import_command_txt(runner, clean_environment, tmp_path):
    """Test the import command from a TXT file."""
    input_file = tmp_path / "import_notes.txt"
    input_file.write_text("Imported Note | Imported Content | Imported Category")
    result = runner.invoke(cli, ["import", "--format", "txt", "--file", str(input_file)])
    assert result.exit_code == 0
    assert "Notes successfully imported" in result.output
    list_result = runner.invoke(cli, ["list"])
    assert "Imported Note" in list_result.output

def test_import_command_csv(runner, clean_environment, tmp_path):
    """Test the import command from a CSV file."""
    input_file = tmp_path / "import_notes.csv"
    input_file.write_text("title,content,category,tags\nImported Note,Imported Content,Imported Category,")
    result = runner.invoke(cli, ["import", "--format", "csv", "--file", str(input_file)])
    assert result.exit_code == 0
    assert "Notes successfully imported" in result.output
    list_result = runner.invoke(cli, ["list"])
    assert "Imported Note" in list_result.output
