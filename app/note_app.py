import os
import csv
import json

class NoteApp:
    def __init__(self, storage_file="notes.json", use_memory=False):
        """Initialize the NoteApp."""
        self.storage_file = storage_file
        self.use_memory = use_memory
        self.notes = [] if use_memory else self._load_notes()

    def _load_notes(self):
        """Load notes from the JSON file."""
        try:
            with open(self.storage_file, "r") as f:
                notes = json.load(f)
                for note in notes:
                    note.setdefault("tags", [])
                return notes
        except FileNotFoundError:
            return []

    def _save_notes(self):
        """Save notes to the JSON file."""
        if not self.use_memory:
            with open(self.storage_file, "w") as f:
                json.dump(self.notes, f, indent=4)

    def add_note(self, title, content, category="General", tags=None):
        """Add a new note with optional tags."""
        if tags is None:
            tags = []
        else:
            tags = [tag.strip().lower() for tag in tags.split(",")]

        note = {"title": title, "content": content, "category": category, "tags": tags}
        self.notes.append(note)
        self._save_notes()
        return f"Note added: {title} - {content} (Category: {category}, Tags: {', '.join(tags)})"

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
                f"{idx + start + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}\n   Tags: {', '.join(note.get('tags', []))}"
                for idx, note in enumerate(paginated_notes)
            ]
        )
        return f"{notes_str}\nPage {page} of {total_pages}."

    def search_notes(self, keyword, category=None, tag=None):
        """Search for notes containing a specific keyword, optionally filtered by category or tag."""
        results = [
            note
            for note in self.notes
            if keyword.lower() in note["title"].lower() or keyword.lower() in note["content"].lower()
        ]

        if category:
            results = [note for note in results if note["category"].lower() == category.lower()]
        if tag:
            results = [note for note in results if tag.lower() in note.get("tags", [])]

        if not results:
            return "No notes found with the given criteria."

        return "\n".join(
            [
                f"{idx + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}\n   Tags: {', '.join(note.get('tags', []))}"
                for idx, note in enumerate(results)
            ]
        )

    def sort_notes(self, sort_by="title"):
        """Sort notes by the specified field."""
        if sort_by not in {"title", "category"}:
            return "Invalid sort field. Please choose 'title' or 'category'."
        
        sorted_notes = sorted(self.notes, key=lambda x: x[sort_by].lower())
        return "\n".join(
            [
                f"{idx + 1}. Title: {note['title']}\n   Content: {note['content']}\n   Category: {note['category']}\n   Tags: {', '.join(note.get('tags', []))}"
                for idx, note in enumerate(sorted_notes)
            ]
        )

    def import_notes(self, file_format="txt", input_file="notes.txt"):
        """Import notes from a file in the specified format."""
        try:
            if file_format == "txt":
                with open(input_file, "r") as f:
                    for line_number, line in enumerate(f, start=1):
                        parts = line.strip().split(" | ")
                        if len(parts) < 3:
                            print(f"Error: Line {line_number} is invalid. Skipping: {line.strip()}")
                            continue
                        title, content, category = parts[:3]
                        tags = ", ".join(parts[3:]) if len(parts) > 3 else None
                        self.add_note(
                            title=title.strip(),
                            content=content.strip(),
                            category=category.strip(),
                            tags=tags,
                        )
                return f"Notes successfully imported from {input_file}."

            elif file_format == "csv":
                with open(input_file, "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.add_note(
                            title=row["title"],
                            content=row["content"],
                            category=row["category"],
                            tags=row.get("tags", ""),
                        )
                return f"Notes successfully imported from {input_file}."

            else:
                return "Unsupported file format. Please choose 'txt' or 'csv'."

        except FileNotFoundError:
            return f"File {input_file} not found."

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
                    f.write(f"   Category: {note['category']}\n")
                    f.write(f"   Tags: {', '.join(note.get('tags', []))}\n\n")
            return f"Notes successfully exported to {output_file}."

        elif file_format == "csv":
            with open(output_file, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["title", "content", "category", "tags"])
                writer.writeheader()
                for note in self.notes:
                    writer.writerow(
                        {
                            "title": note["title"],
                            "content": note["content"],
                            "category": note["category"],
                            "tags": ", ".join(note.get("tags", [])),
                        }
                    )
            return f"Notes successfully exported to {output_file}."

        else:
            return "Unsupported file format. Please choose 'txt' or 'csv'."
