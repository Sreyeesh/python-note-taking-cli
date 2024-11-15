from app.note_app import NoteApp
import os

def setup_test_file(storage_file):
    """Ensure the test file exists to avoid FileNotFoundError."""
    if not os.path.exists(storage_file):
        with open(storage_file, "w") as file:
            file.write("[]")  # Initialize with an empty JSON array

def cleanup_test_file(storage_file):
    """Remove the test file after each test."""
    if os.path.exists(storage_file):
        os.remove(storage_file)

def test_add_note():
    storage_file = "test_notes.json"
    setup_test_file(storage_file)

    app = NoteApp(storage_file=storage_file)
    result = app.add_note("Test Note", "This is a test.")
    assert result == "Note added: Test Note"
    assert len(app.notes) == 1
    assert app.notes[0]["title"] == "Test Note"

    cleanup_test_file(storage_file)

def test_view_notes():
    storage_file = "test_notes.json"
    setup_test_file(storage_file)

    app = NoteApp(storage_file=storage_file)
    app.add_note("Test Note", "This is a test.")
    result = app.view_notes()
    assert "Test Note" in result
    assert "This is a test." in result

    cleanup_test_file(storage_file)

def test_view_notes_empty():
    storage_file = "test_notes.json"
    setup_test_file(storage_file)

    app = NoteApp(storage_file=storage_file)
    result = app.view_notes()
    assert result == "No notes available."

    cleanup_test_file(storage_file)

def test_delete_note():
    storage_file = "test_notes.json"
    setup_test_file(storage_file)

    app = NoteApp(storage_file=storage_file)
    app.add_note("Test Note", "This is a test.")
    result = app.delete_note("Test Note")
    assert result == "Note deleted: Test Note"
    assert len(app.notes) == 0

    cleanup_test_file(storage_file)

def test_delete_nonexistent_note():
    storage_file = "test_notes.json"
    setup_test_file(storage_file)

    app = NoteApp(storage_file=storage_file)
    result = app.delete_note("Nonexistent Note")
    assert result == "Note not found: Nonexistent Note"

    cleanup_test_file(storage_file)
