import pytest
from app.note_app import NoteApp


@pytest.fixture
def app():
    """Fixture to create a NoteApp instance in memory for testing."""
    return NoteApp(use_memory=True)


def test_add_note_success(app):
    """Test adding a note successfully."""
    result = app.add_note("Test Title", "Test Content", "Test Category", "tag1, tag2")
    assert len(app.notes) == 1
    assert app.notes[0]["title"] == "Test Title"
    assert app.notes[0]["tags"] == ["tag1", "tag2"]
    assert (
        result == "Note added: Test Title - Test Content "
        "(Category: Test Category, Tags: tag1, tag2)"
    )


def test_add_note_empty_title(app):
    """Test adding a note with an empty title."""
    with pytest.raises(ValueError):
        app.add_note("", "Test Content")


def test_delete_note_success(app):
    """Test deleting a note successfully."""
    app.add_note("Test Title", "Test Content", "Test Category")
    result = app.delete_note("Test Title")
    assert result == "Note with title 'Test Title' has been deleted."
    assert len(app.notes) == 0
