import os


def reset_storage():
    """Reset the storage file to an empty state."""
    storage_file = os.path.expanduser("~/.note-cli/data/notes.json")
    if os.path.exists(storage_file):
        os.remove(storage_file)
