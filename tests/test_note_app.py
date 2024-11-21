# tests/test_note_app.py

import pytest
from app.note_app import NoteApp

@pytest.fixture
def app():
    # Use in-memory storage for testing
    return NoteApp(use_memory=True)

def test_add_note(app):
    result = app.add_note("Test Title", "Test Content", "Test Category")
    assert len(app.notes) == 1
    assert result == "Note added: Test Title - Test Content (Category: Test Category)"

def test_view_notes(app):
    app.add_note("Test Title", "Test Content", "Test Category")
    result = app.view_notes()
    assert "Test Title" in result

def test_delete_note_success(app):
    app.add_note("Test Title", "Test Content", "Test Category")
    result = app.delete_note("Test Title")
    assert result == "Note with title 'Test Title' has been deleted."

def test_delete_note_failure(app):
    result = app.delete_note("Nonexistent Title")
    assert result == "Note with title 'Nonexistent Title' not found."
