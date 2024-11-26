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

    def search_notes(self, keyword, category=None):
        """Search for notes by keyword and optionally filter by category."""
        results = [
            note for note in self.notes
            if keyword.lower() in note["title"].lower() or keyword.lower() in note["content"].lower()
        ]
        if category:  # Filter results by category if provided
            results = [note for note in results if note["category"].lower() == category.lower()]

        if not results:
            return "No notes found with the given keyword and category."
        
        return "\n".join(
            [
                f"{idx + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}"
                for idx, note in enumerate(results)
            ]
        )


    def view_notes(self, page=1, limit=5):
        """Return a paginated list of notes."""
        total_notes = len(self.notes)
        total_pages = (total_notes + limit - 1) // limit  # Calculate total pages
        start = (page - 1) * limit
        end = start + limit

        if start >= total_notes:
            return f"No notes found on page {page}. Total pages: {total_pages}."

        paginated_notes = self.notes[start:end]
        notes_str = "\n".join(
            [
                f"{idx + start + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}"
                for idx, note in enumerate(paginated_notes)
            ]
        )
        return f"{notes_str}\nPage {page} of {total_pages}."

    def view_notes_by_category(self, category, page=1, limit=5):
            """Return a paginated list of notes filtered by category."""
            filtered_notes = [note for note in self.notes if note["category"].lower() == category.lower()]
            total_notes = len(filtered_notes)
            total_pages = (total_notes + limit - 1) // limit
            start = (page - 1) * limit
            end = start + limit

            if start >= total_notes:
                return f"No notes found in category '{category}' on page {page}. Total pages: {total_pages}."

            paginated_notes = filtered_notes[start:end]
            notes_str = "\n".join(
                [
                    f"{idx + start + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}"
                    for idx, note in enumerate(paginated_notes)
                ]
            )
            return f"{notes_str}\nPage {page} of {total_pages}."
    
    def test_view_notes_with_pagination(app):
        for i in range(10):
            app.add_note(f"Note {i+1}", f"Content {i+1}", "General")
        result = app.view_notes(page=1, limit=5)
        assert "Page 1 of 2." in result

def test_view_notes_by_category_with_pagination(app):
    for i in range(10):
        app.add_note(f"Note {i+1}", f"Content {i+1}", "Work")
    result = app.view_notes_by_category("Work", page=2, limit=5)
    assert "Page 2 of 2." in result

