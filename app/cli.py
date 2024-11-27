import click
from app.note_app import NoteApp

# Use a global note_app instance by default
note_app = NoteApp()

def get_note_app(memory_only=False):
    """Retrieve the NoteApp instance, optionally in memory-only mode."""
    global note_app
    if memory_only:
        note_app = NoteApp(use_memory=True)
    return note_app

@click.group()
@click.option("--memory-only", is_flag=True, help="Use memory-only mode for testing.")
def cli(memory_only):
    """Note Taking CLI Application."""
    get_note_app(memory_only)

@cli.command(name="add")
@click.argument("title")
@click.argument("content")
@click.option("--category", default="General", help="Category for the note")
@click.option("--tags", default=None, help="Comma-separated tags for the note")
def add_note(title, content, category, tags):
    """Add a new note."""
    result = note_app.add_note(title, content, category, tags)
    click.echo(result)

@cli.command(name="list")
@click.option("--page", default=1, help="Page number to display")
@click.option("--limit", default=5, help="Number of notes per page")
def list_notes(page, limit):
    """List notes with pagination."""
    result = note_app.view_notes(page=page, limit=limit)
    click.echo(result)

@cli.command(name="delete")
@click.argument("title")
def delete_note(title):
    """Delete a note by title."""
    result = note_app.delete_note(title)
    click.echo(result)
