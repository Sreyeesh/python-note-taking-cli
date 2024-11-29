import click
from app.note_app import NoteApp

note_app_instance = None  # Use a global instance to ensure a single NoteApp is used

def get_note_app(memory_only=False):
    """Retrieve the NoteApp instance, optionally in memory-only mode."""
    global note_app_instance
    if note_app_instance is None or memory_only:
        note_app_instance = NoteApp(use_memory=memory_only)
    return note_app_instance


@click.group()
@click.option("--memory-only", is_flag=True, help="Use memory-only mode for testing.")
def cli(memory_only):
    """Note Taking CLI Application."""
    get_note_app(memory_only)

@cli.command()
@click.argument("title")
@click.argument("content")
@click.option("--category", default="General", help="Category of the note.")
@click.option("--tags", default="", help="Comma-separated tags for the note.")
def add(title, content, category, tags):
    """Add a new note."""
    try:
        tags_list = [tag.strip() for tag in tags.split(",") if tag.strip()]
        result = get_note_app().add_note(title, content, category, tags_list)
        click.echo(result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@cli.command(name="list")
@click.option("--page", default=1, help="Page number to display.")
@click.option("--limit", default=5, help="Number of notes per page.")
def list_notes(page, limit):
    """List notes with pagination."""
    result = get_note_app().view_notes(page=page, limit=limit)
    click.echo(result)

@cli.command(name="delete")
@click.argument("title")
def delete(title):
    """Delete a note by title."""
    result = get_note_app().delete_note(title)
    click.echo(result)
