import pytest
from click.testing import CliRunner
from app.cli import cli

@pytest.fixture
def runner():
    """Fixture to create a CLI runner for testing."""
    return CliRunner()

def test_add_command(runner):
    """Test the add command."""
    result = runner.invoke(cli, ["add", "CLI Title", "CLI Content", "--category", "Work", "--tags", "tag1,tag2"])
    assert result.exit_code == 0
    assert "Note added: CLI Title" in result.output

def test_list_command(runner):
    """Test the list command."""
    runner.invoke(cli, ["add", "Note 1", "Content 1", "--category", "Personal"])
    runner.invoke(cli, ["add", "Note 2", "Content 2", "--category", "Work"])
    result = runner.invoke(cli, ["list", "--page", "1", "--limit", "2"])
    assert result.exit_code == 0
    assert "Note 1" in result.output
    assert "Note 2" in result.output

def test_delete_command(runner):
    """Test the delete command."""
    runner.invoke(cli, ["add", "Delete Me", "To be deleted"])
    result = runner.invoke(cli, ["delete", "Delete Me"])
    assert result.exit_code == 0
    assert "Note with title 'Delete Me' has been deleted." in result.output
    result = runner.invoke(cli, ["list"])
    assert "Delete Me" not in result.output

def test_search_command(runner):
    """Test the search command."""
    runner.invoke(cli, ["add", "Search Me", "Find this content", "--category", "Search"])
    result = runner.invoke(cli, ["search", "Search"])
    assert result.exit_code == 0
    assert "Search Me" in result.output

def test_search_with_category_command(runner):
    """Test the search command with category filter."""
    runner.invoke(cli, ["add", "Search Category", "Category Content", "--category", "Specific"])
    result = runner.invoke(cli, ["search", "Category", "--category", "Specific"])
    assert result.exit_code == 0
    assert "Search Category" in result.output

def test_view_tag_command(runner):
    """Test the view-tag command."""
    runner.invoke(cli, ["add", "Tagged Note", "Content with tag", "--tags", "tag1,tag2"])
    result = runner.invoke(cli, ["view-tag", "tag1"])
    assert result.exit_code == 0
    assert "Tagged Note" in result.output

def test_export_command_txt(runner, tmp_path):
    """Test the export command to a TXT file."""
    runner.invoke(cli, ["add", "Exported Note", "This will be exported"])
    output_file = tmp_path / "notes.txt"
    result = runner.invoke(cli, ["export", "--format", "txt", "--output", str(output_file)])
    assert result.exit_code == 0
    assert f"Notes successfully exported to {output_file}" in result.output
    assert output_file.read_text()

def test_export_command_csv(runner, tmp_path):
    """Test the export command to a CSV file."""
    runner.invoke(cli, ["add", "Exported Note", "This will be exported"])
    output_file = tmp_path / "notes.csv"
    result = runner.invoke(cli, ["export", "--format", "csv", "--output", str(output_file)])
    assert result.exit_code == 0
    assert f"Notes successfully exported to {output_file}" in result.output
    assert output_file.read_text()

def test_import_command_txt(runner, tmp_path):
    """Test the import command from a TXT file."""
    input_file = tmp_path / "import_notes.txt"
    input_file.write_text("Imported Note | Imported Content | Imported Category")
    result = runner.invoke(cli, ["import", "--format", "txt", "--file", str(input_file)])
    assert result.exit_code == 0
    assert "Notes successfully imported" in result.output
    list_result = runner.invoke(cli, ["list"])
    assert "Imported Note" in list_result.output

def test_import_command_csv(runner, tmp_path):
    """Test the import command from a CSV file."""
    input_file = tmp_path / "import_notes.csv"
    input_file.write_text("title,content,category,tags\nImported Note,Imported Content,Imported Category,")
    result = runner.invoke(cli, ["import", "--format", "csv", "--file", str(input_file)])
    assert result.exit_code == 0
    assert "Notes successfully imported" in result.output
    list_result = runner.invoke(cli, ["list"])
    assert "Imported Note" in list_result.output
