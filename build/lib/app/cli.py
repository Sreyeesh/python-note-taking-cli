import click
from app.note_app import NoteApp  # Use absolute import

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


@cli.command()
@click.argument("title")
@click.argument("content")
@click.option("--category", default="General", help="Category of the note.")
@click.option("--tags", default="", help="Comma-separated tags for the note.")
def add(title, content, category, tags):
    """Add a new note."""
    try:
        tags_list = [tag.strip() for tag in tags.split(",") if tag.strip()]
        result = note_app.add_note(title, content, category, tags_list)
        click.echo(result)
    except ValueError as e:
        click.echo(f"Error: {e}")


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
    try:
        result = note_app.delete_note(title)
        click.echo(result)
    except ValueError as e:
        click.echo(f"Error: {e}")
