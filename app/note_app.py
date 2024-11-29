import os
import json


class NoteApp:
    def __init__(self, storage_file="data/notes.json", use_memory=False):
        """Initialize the NoteApp."""
        base_dir = os.path.expanduser("~/.note-cli")  # Store in user's home directory
        self.storage_file = os.path.join(base_dir, storage_file)  # Path to notes.json
        self.use_memory = use_memory
        self.notes = [] if use_memory else self._load_notes()

    def _load_notes(self):
        """Load notes from the JSON file."""
        print(f"Loading notes from: {self.storage_file}")
        try:
            with open(self.storage_file, "r") as f:
                notes = json.load(f)
                for note in notes:
                    note.setdefault("tags", [])
                return notes
        except FileNotFoundError:
            print(f"Storage file not found: {self.storage_file}. Returning an empty list.")
            return []

    def _save_notes(self):
        """Save notes to the JSON file."""
        print(f"Saving notes to: {self.storage_file}")
        os.makedirs(os.path.dirname(self.storage_file), exist_ok=True)
        with open(self.storage_file, "w") as f:
            json.dump(self.notes, f, indent=4)
        print(f"Notes saved: {self.notes}")

    def add_note(self, title, content, category="General", tags=None):
        """Add a new note."""
        if not title.strip():
            raise ValueError("Title cannot be empty.")

        if any(note["title"].lower() == title.lower() for note in self.notes):
            raise ValueError(f"A note with the title '{title}' already exists.")

        new_note = {
            "title": title,
            "content": content,
            "category": category,
            "tags": tags or []
        }
        self.notes.append(new_note)
        self._save_notes()
        return f"Note added: {title} - {content} (Category: {category}, Tags: {', '.join(tags or [])})"

    def delete_note(self, title):
        """Delete a note by title."""
        for note in self.notes:
            if note["title"].lower() == title.lower():
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
