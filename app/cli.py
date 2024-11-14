# app/cli.py

import click
from app.note_app import NoteApp

# Initialize NoteApp instance
app = NoteApp()

@click.group()
def cli():
    """A simple CLI for managing notes."""
    pass

@cli.command()
@click.argument("title")
@click.argument("content")
def add(title, content):
    """Add a new note with TITLE and CONTENT."""
    result = app.add_note(title, content)
    click.echo(result)

@cli.command()
def view():
    """View all notes."""
    result = app.view_notes()
    click.echo(result)

@cli.command()
@click.argument("index", type=int)
@click.argument("new_title")
@click.argument("new_content")
def update(index, new_title, new_content):
    """Update a note at INDEX with NEW_TITLE and NEW_CONTENT."""
    result = app.update_note(index - 1, new_title, new_content)
    click.echo(result)

@cli.command()
@click.argument("index", type=int)
def delete(index):
    """Delete a note at INDEX."""
    result = app.delete_note(index - 1)
    click.echo(result)


@cli.command()
@click.argument("keyword")
def search(keyword):
    """Search for notes containing a keyword."""
    result = app.search_notes(keyword)
    click.echo(result)

@cli.command()
@click.argument("category")
def view_category(category):
    """View all notes in a specific category."""
    result = app.view_by_category(category)
    click.echo(result)
