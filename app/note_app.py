# app/note_app.py

class NoteApp:
    def __init__(self):
        # Initialize an empty list to store notes
        self.notes = []

    def add_note(self, title, content, category=None):
        """Add a note with a title, content, and optional category."""
        note = {"title": title, "content": content, "category": category}
        self.notes.append(note)
        return f"Note added: {title} (Category: {category or 'Uncategorized'})"

    def view_by_category(self, category):
        """View notes by category."""
        results = [note for note in self.notes if note.get("category") == category]
        if results:
            output = f"Notes in category '{category}':\n"
            for i, note in enumerate(results, 1):
                output += f"{i}. {note['title']} - {note['content']}\n"
            return output.strip()
        else:
            return f"No notes found in category '{category}'."


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


# app/note_app.py

def search_notes(self, keyword):
    """Search for notes that contain a specific keyword."""
    results = [note for note in self.notes if keyword.lower() in note['title'].lower() or keyword.lower() in note['content'].lower()]
    if results:
        output = "Search Results:\n"
        for i, note in enumerate(results, 1):
            output += f"{i}. {note['title']} - {note['content']}\n"
        return output.strip()
    else:
        return "No matching notes found."

def add_note_with_category(self, title, content, category="General"):
        note = {"title": title, "content": content, "category": category}
        self.notes.append(note)
        return f"Note added: {title} (Category: {category})"