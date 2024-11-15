from app.note_app import NoteApp

def test_add_note():
    app = NoteApp()
    result = app.add_note("Test", "This is a test.")
    assert result == "Note added: Test (Category: Uncategorized)"
