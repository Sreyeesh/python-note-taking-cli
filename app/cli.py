import click
from app.note_app import NoteApp

note_app = NoteApp()

@click.group()
def cli():
    pass

@cli.command()
@click.argument("title")
@click.argument("content")
def add(title, content):
    result = note_app.add_note(title, content)
    click.echo(result)

@cli.command()
def list():
    result = note_app.view_notes()
    click.echo(result)

@cli.command()
@click.argument("title")
def delete(title):
    result = note_app.delete_note(title)
    click.echo(result)

if __name__ == "__main__":
    cli()
