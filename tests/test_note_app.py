import pytest
from app.note_app import NoteApp


@pytest.fixture
def app():
    """Fixture to initialize NoteApp with memory-only mode for testing."""
    return NoteApp(use_memory=True)


def test_add_note_success(app):
    """Test adding a note successfully."""
    result = app.add_note("Test Title", "Test Content", "Test Category", ["tag1", "tag2"])
    assert len(app.notes) == 1
    assert app.notes[0]["title"] == "Test Title"
    assert app.notes[0]["content"] == "Test Content"
    assert app.notes[0]["category"] == "Test Category"
    assert app.notes[0]["tags"] == ["tag1", "tag2"]
    assert result == "Note added: Test Title - Test Content (Category: Test Category, Tags: tag1, tag2)"


def test_add_note_duplicate_title(app):
    """Test adding a note with a duplicate title."""
    app.add_note("Test Title", "Test Content")
    with pytest.raises(ValueError, match="A note with the title 'Test Title' already exists."):
        app.add_note("Test Title", "Another Content")


def test_delete_note_success(app):
    """Test deleting a note successfully."""
    app.add_note("Test Title", "Test Content")
    result = app.delete_note("Test Title")
    assert len(app.notes) == 0
    assert result == "Note with title 'Test Title' has been deleted."


def test_delete_note_not_found(app):
    """Test deleting a note that does not exist."""
    result = app.delete_note("Nonexistent Note")
    assert result == "Note with title 'Nonexistent Note' not found."


def test_view_notes_pagination(app):
    """Test viewing notes with pagination."""
    for i in range(15):
        app.add_note(f"Title {i + 1}", f"Content {i + 1}")
    result = app.view_notes(page=1, limit=5)
    assert "Page 1 of 3" in result
    assert "Title 1" in result
    assert "Title 5" in result


def test_view_notes_no_results(app):
    """Test viewing notes when no notes exist."""
    result = app.view_notes()
    assert result == "No notes found on page 1. Total pages: 0."
