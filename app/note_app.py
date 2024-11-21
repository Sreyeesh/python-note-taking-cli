# app/note_app.py

import json

# app/note_app.py

class NoteApp:
    def __init__(self, storage_file="notes.json", use_memory=False):
        """
        Initialize the NoteApp.

        :param storage_file: Path to the JSON storage file.
        :param use_memory: If True, use in-memory storage for testing.
        """
        self.storage_file = storage_file
        self.use_memory = use_memory
        self.notes = [] if use_memory else self._load_notes()

    def _load_notes(self):
        """Load notes from the JSON file."""
        try:
            with open(self.storage_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save_notes(self):
        """Save notes to the JSON file."""
        if not self.use_memory:  # Skip saving during tests
            with open(self.storage_file, "w") as f:
                json.dump(self.notes, f, indent=4)

    def add_note(self, title, content, category="General"):
        """Add a new note and save to storage."""
        note = {"title": title, "content": content, "category": category}
        self.notes.append(note)
        self._save_notes()
        return f"Note added: {title} - {content} (Category: {category})"

    # Other methods (view_notes, delete_note, etc.) remain unchanged


    def view_notes(self):
        """Return a string listing all notes."""
        if not self.notes:
            return "No notes available."
        return "\n".join(
            [
                f"{idx + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}"
                for idx, note in enumerate(self.notes)
            ]
        )

    def delete_note(self, title):
        """Delete a note by title and save changes."""
        for note in self.notes:
            if note["title"].lower() == title.lower():
                self.notes.remove(note)
                self._save_notes()
                return f"Note with title '{title}' has been deleted."
        return f"Note with title '{title}' not found."

    def search_notes(self, keyword):
        """Search for notes by a keyword in title or content."""
        results = [
            note
            for note in self.notes
            if keyword.lower() in note["title"].lower() or keyword.lower() in note["content"].lower()
        ]
        if not results:
            return "No notes found with that keyword."
        return "\n".join(
            [
                f"{idx + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}"
                for idx, note in enumerate(results)
            ]
        )

    def view_notes_by_category(self, category):
        """View notes filtered by a specific category."""
        results = [note for note in self.notes if note["category"].lower() == category.lower()]
        if not results:
            return f"No notes found in category '{category}'."
        return "\n".join(
            [
                f"{idx + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}"
                for idx, note in enumerate(results)
            ]
        )
