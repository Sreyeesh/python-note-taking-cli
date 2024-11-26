import click
from app.note_app import NoteApp

note_app = NoteApp()

@click.group()
def cli():
    """Note Taking CLI Application."""
    pass

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
@click.option("--sort-by", default=None, help="Field to sort by (title or category)")
def list_notes(page, limit, sort_by):
    """List notes with pagination and sorting."""
    if sort_by:
        result = note_app.sort_notes(sort_by=sort_by)
    else:
        result = note_app.view_notes(page=page, limit=limit)
    click.echo(result)

@cli.command(name="delete")
@click.argument("title")
def delete_note(title):
    """Delete a note by title."""
    result = note_app.delete_note(title)
    click.echo(result)

@cli.command(name="search")
@click.argument("keyword")
@click.option("--category", default=None, help="Optional category to filter the search results")
@click.option("--tag", default=None, help="Optional tag to filter the search results")
def search_notes(keyword, category, tag):
    """Search notes by keyword, category, or tag."""
    result = note_app.search_notes(keyword, category, tag)
    click.echo(result)

@cli.command(name="view-tag")
@click.argument("tag")
def view_notes_by_tag(tag):
    """View notes by tag."""
    result = note_app.search_by_tag(tag)
    click.echo(result)

@cli.command(name="export")
@click.option("--format", default="txt", help="File format: txt or csv")
@click.option("--output", default="notes.txt", help="Output file name")
def export_notes(format, output):
    """Export notes to a file."""
    result = note_app.export_notes(file_format=format, output_file=output)
    click.echo(result)

@cli.command(name="import")
@click.option("--format", default="txt", help="File format: txt or csv")
@click.option("--file", default="notes.txt", help="Input file name")
def import_notes(format, file):
    """Import notes from a file."""
    result = note_app.import_notes(file_format=format, input_file=file)
    click.echo(result)

if __name__ == "__main__":
    cli()
