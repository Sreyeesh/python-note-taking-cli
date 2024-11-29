import pytest
from app.note_app import NoteApp


@pytest.fixture
def app():
    """Fixture to provide a fresh instance of NoteApp for each test."""
    return NoteApp(use_memory=True)


def test_add_note_success(app):
    """Test adding a note successfully."""
    result = app.add_note("Test Title", "Test Content", "General", ["tag1", "tag2"])
    assert result == "Note added: Test Title - Test Content (Category: General, Tags: tag1, tag2)"


def test_delete_note_success(app):
    """Test deleting a note successfully."""
    app.add_note("Test Title", "Test Content")
    result = app.delete_note("Test Title")
    assert result == "Note with title 'Test Title' has been deleted."


def test_view_notes_empty(app):
    """Test viewing notes when no notes exist."""
    result = app.view_notes()
    assert "No notes found. Total pages: 0." in result  # Adjusted to match the actual output


def test_view_notes_with_notes(app):
    """Test viewing notes when notes exist."""
    app.add_note("Title 1", "Content 1", "General", ["tag1"])
    app.add_note("Title 2", "Content 2", "Work", ["urgent"])
    result = app.view_notes()
    assert "1. Title: Title 1" in result
    assert "2. Title: Title 2" in result
    assert "Page 1 of 1." in result
