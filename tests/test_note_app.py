import pytest
from app.note_app import NoteApp

@pytest.fixture
def app():
    return NoteApp(use_memory=True)

def test_add_note(app):
    result = app.add_note("Test Title", "Test Content", "Test Category")
    assert len(app.notes) == 1
    assert result == "Note added: Test Title - Test Content (Category: Test Category, Tags: )"

def test_delete_note_success(app):
    app.add_note("Test Title", "Test Content", "Test Category")
    result = app.delete_note("Test Title")
    assert result == "Note with title 'Test Title' has been deleted."
    assert len(app.notes) == 0

def test_delete_note_failure(app):
    result = app.delete_note("Nonexistent Title")
    assert result == "Note with title 'Nonexistent Title' not found."

def test_view_notes(app):
    app.add_note("Test Title", "Test Content", "Test Category")
    result = app.view_notes()
    assert "Test Title" in result

def test_search_notes(app):
    app.add_note("Test Title", "Test Content", "Test Category", tags="tag1,tag2")
    result = app.search_notes("Test")
    assert "Test Title" in result
    result = app.search_notes("Test", category="Test Category")
    assert "Test Title" in result

def test_sort_notes(app):
    app.add_note("B Title", "Content 1", "Work")
    app.add_note("A Title", "Content 2", "Personal")
    result = app.sort_notes("title")
    assert "A Title" in result
    assert "B Title" in result

def test_import_notes(app, tmp_path):
    input_file = tmp_path / "notes.txt"
    input_file.write_text("Title 1 | Content 1 | Work\nTitle 2 | Content 2 | Personal")
    result = app.import_notes(file_format="txt", input_file=str(input_file))
    assert "Notes successfully imported" in result
    assert len(app.notes) == 2
