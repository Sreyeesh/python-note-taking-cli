import json
import os

class NoteApp:
    def __init__(self, storage_file="notes.json"):
        self.storage_file = storage_file
        self.notes = self.load_notes()

    def load_notes(self):
        """Load notes from the JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as file:
                return json.load(file)
        return []

    def save_notes(self):
        """Save notes to the JSON file."""
        with open(self.storage_file, "w") as file:
            json.dump(self.notes, file)

    def add_note(self, title, content):
        """Add a new note to the application."""
        note = {"title": title, "content": content}
        self.notes.append(note)
        self.save_notes()
        return f"Note added: {title}"

    def view_notes(self):
        """View all notes."""
        if not self.notes:
            return "No notes available."
        return "\n".join([f"{i + 1}. Title: {note['title']}, Content: {note['content']}" for i, note in enumerate(self.notes)])

    def delete_note(self, title):
        """Delete a note by its title."""
        for note in self.notes:
            if note["title"] == title:
                self.notes.remove(note)
                self.save_notes()
                return f"Note deleted: {title}"
        return f"Note not found: {title}"
