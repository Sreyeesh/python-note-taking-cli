import click
from app.note_app import NoteApp

@click.group()
@click.option("--memory-only", is_flag=True, help="Use memory-only mode for testing.")
@click.pass_context
def cli(ctx, memory_only):
    """Note Taking CLI Application."""
    ctx.obj = NoteApp(use_memory=memory_only)


@cli.command()
@click.argument("title")
@click.argument("content")
@click.option("--category", default="General", help="Note category")
@click.option("--tags", default="", help="Comma-separated tags")
@click.pass_obj
def add(note_app, title, content, category, tags):
    """Add a new note."""
    tags_list = tags.split(",") if tags else []
    try:
        result = note_app.add_note(title, content, category, tags_list)
        click.echo(result)
    except ValueError as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument("title")
@click.pass_obj
def delete(note_app, title):
    """Delete a note by title."""
    result = note_app.delete_note(title)
    click.echo(result)


@cli.command(name="list")
@click.option("--page", default=1, help="Page number to view", type=int)
@click.option("--limit", default=5, help="Number of notes per page", type=int)
@click.pass_obj
def list_notes(note_app, page, limit):
    """List notes with pagination."""
    try:
        result = note_app.view_notes(page, limit)
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}")
