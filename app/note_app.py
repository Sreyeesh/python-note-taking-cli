# app/note_app.py

class NoteApp:
    def __init__(self):
        # Initialize an empty list to store notes
        self.notes = []

    def add_note(self, title, content):
        """Add a note with a title and content."""
        note = {"title": title, "content": content}
        self.notes.append(note)
        return f"Note added: {title}"

    def view_notes(self):
        """Return a string listing all notes, or a message if no notes are available."""
        if not self.notes:
            return "No notes available."
        output = "Notes:\n"
        for i, note in enumerate(self.notes, 1):
            output += f"{i}. {note['title']} - {note['content']}\n"
        return output.strip()

    def update_note(self, index, new_title, new_content):
        """Update a note's title and content by index."""
        if 0 <= index < len(self.notes):
            self.notes[index]["title"] = new_title
            self.notes[index]["content"] = new_content
            return f"Note {index + 1} updated."
        else:
            return "Note not found."

    def delete_note(self, index):
        """Delete a note by index."""
        if 0 <= index < len(self.notes):
            removed_note = self.notes.pop(index)
            return f"Note deleted: {removed_note['title']}"
        else:
            return "Note not found."
