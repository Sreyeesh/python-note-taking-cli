import os
import json


class NoteApp:
    def __init__(self, storage_file=None, use_memory=False):
        """Initialize the NoteApp."""
        self.use_memory = use_memory
        self.notes = []

        if not use_memory:
            base_dir = os.path.expanduser("~/.note-cli/data")
            os.makedirs(base_dir, exist_ok=True)
            self.storage_file = storage_file or os.path.join(base_dir, "notes.json")
            self.notes = self._load_notes()

    def _load_notes(self):
        """Load notes from the storage file."""
        try:
            with open(self.storage_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_notes(self):
        """Save notes to the storage file."""
        if not self.use_memory:
            with open(self.storage_file, "w") as f:
                json.dump(self.notes, f, indent=4)

    def add_note(self, title, content, category="General", tags=None):
        """Add a new note."""
        if any(note["title"] == title for note in self.notes):
            raise ValueError(f"A note with the title '{title}' already exists.")
        note = {
            "title": title,
            "content": content,
            "category": category,
            "tags": tags or []
        }
        self.notes.append(note)
        self._save_notes()
        return f"Note added: {title} - {content} (Category: {category}, Tags: {', '.join(note['tags'])})"

    def delete_note(self, title):
        """Delete a note by title."""
        for note in self.notes:
            if note["title"] == title:
                self.notes.remove(note)
                self._save_notes()
                return f"Note with title '{title}' has been deleted."
        return f"Note with title '{title}' not found."

    def view_notes(self, page=1, limit=5):
        """Return a paginated list of notes."""
        total_notes = len(self.notes)
        total_pages = (total_notes + limit - 1) // limit
        start = (page - 1) * limit
        end = start + limit

        if total_notes == 0:
            return f"No notes found. Total pages: {total_pages}."

        if start >= total_notes:
            return f"No notes found on page {page}. Total pages: {total_pages}."

        paginated_notes = self.notes[start:end]
        notes_str = "\n".join(
            [
                f"{idx + start + 1}. Title: {note['title']}\n"
                f"   Content: {note['content']}\n"
                f"   Category: {note['category']}\n"
                f"   Tags: {', '.join(note.get('tags', []))}"
                for idx, note in enumerate(paginated_notes)
            ]
        )
        return f"{notes_str}\nPage {page} of {total_pages}."
