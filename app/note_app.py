import os
import csv
import json

class NoteApp:
    def __init__(self, storage_file="notes.json", use_memory=False):
        """Initialize the NoteApp."""
        self.storage_file = storage_file
        self.use_memory = use_memory
        # Initialize notes as an empty list or load from the storage file
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
        if not self.use_memory:
            with open(self.storage_file, "w") as f:
                json.dump(self.notes, f, indent=4)

    def add_note(self, title, content, category="General"):
        """Add a new note."""
        note = {"title": title, "content": content, "category": category}
        self.notes.append(note)
        self._save_notes()
        return f"Note added: {title} - {content} (Category: {category})"

    def delete_note(self, title):
        """Delete a note by title."""
        for note in self.notes:
            if note["title"].lower() == title.lower():
                self.notes.remove(note)
                self._save_notes()
                return f"Note with title '{title}' has been deleted."
        return f"Note with title '{title}' not found."

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
    def search_notes(self, keyword, category=None):
        """Search for notes containing a specific keyword, optionally filtered by category."""
        results = [
            note
            for note in self.notes
            if keyword.lower() in note["title"].lower() or keyword.lower() in note["content"].lower()
        ]

        if category:
            results = [note for note in results if note["category"].lower() == category.lower()]

        if not results:
            return "No notes found with the given criteria."
        
        return "\n".join(
            [
                f"{idx + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}"
                for idx, note in enumerate(results)
            ]
        )


    def view_notes_by_category(self, category):
        """Return a string listing notes filtered by category."""
        results = [note for note in self.notes if note["category"].lower() == category.lower()]
        if not results:
            return f"No notes found in category '{category}'."
        return "\n".join(
            [
                f"{idx + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}"
                for idx, note in enumerate(results)
            ]
        )

    def export_notes(self, file_format="txt", output_file="notes.txt"):
        """Export notes to a file in the specified format."""
        if not self.notes:
            return "No notes available to export."

        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        if file_format == "txt":
            with open(output_file, "w") as f:
                for idx, note in enumerate(self.notes):
                    f.write(f"{idx + 1}. Title: {note['title']}\n")
                    f.write(f"   Content: {note['content']}\n")
                    f.write(f"   Category: {note['category']}\n\n")
            return f"Notes successfully exported to {output_file}."

        elif file_format == "csv":
            with open(output_file, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["title", "content", "category"])
                writer.writeheader()
                writer.writerows(self.notes)
            return f"Notes successfully exported to {output_file}."

        else:
            return "Unsupported file format. Please choose 'txt' or 'csv'."
