import click
from app.note_app import NoteApp

# Create an instance of NoteApp
note_app = NoteApp()

@click.group()
def cli():
    """Note Taking CLI Application."""
    pass

@cli.command(name="add")
@click.argument("title")
@click.argument("content")
@click.option("--category", default="General", help="Category for the note")
def add_note(title, content, category):
    """
    Add a new note.

    Example:
    python main.py add "Shopping List" "Buy milk and eggs" --category "Personal"
    """
    result = note_app.add_note(title, content, category)
    click.echo(result)

@cli.command(name="list")
def list_notes():
    """
    List all notes.

    Example:
    python main.py list
    """
    result = note_app.view_notes()
    click.echo(result)

@cli.command(name="delete")
@click.argument("title")
def delete_note(title):
    """
    Delete a note by title.

    Example:
    python main.py delete "Shopping List"
    """
    result = note_app.delete_note(title)
    click.echo(result)

@cli.command(name="search")
@click.argument("keyword")
@click.option("--category", default=None, help="Optional category to filter the search results")
def search_notes(keyword, category):
    """
    Search for notes containing a specific keyword, optionally filtered by category.

    Example:
    python main.py search "milk"
    python main.py search "milk" --category "Personal"
    """
    result = note_app.search_notes(keyword, category)
    click.echo(result)


@cli.command(name="export")
@click.option("--format", default="txt", help="File format: txt or csv")
@click.option("--output", default="notes.txt", help="Output file name")
def export_notes(format, output):
    """
    Export notes to a file in the specified format.

    Example:
    python main.py export --format txt --output notes.txt
    python main.py export --format csv --output notes.csv
    """
    result = note_app.export_notes(file_format=format, output_file=output)
    click.echo(result)
