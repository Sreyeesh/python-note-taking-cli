# app/cli.py

import click
from app.note_app import NoteApp

# Shared instance of NoteApp
note_app = NoteApp()

@click.group()
def cli():
    """Note Taking CLI Application"""
    pass

@cli.command(name="add")
@click.argument("title")
@click.argument("content")
@click.option("--category", default="General", help="Category for the note")
def add_note(title, content, category):
    """
    Add a new note with a title, content, and optional category.

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
    Delete a note by its title.

    Example:
    python main.py delete "Shopping List"
    """
    result = note_app.delete_note(title)
    click.echo(result)

@cli.command(name="search")
@click.argument("keyword")
def search_notes(keyword):
    """
    Search for notes containing a specific keyword.

    Example:
    python main.py search "milk"
    """
    result = note_app.search_notes(keyword)
    click.echo(result)

@cli.command(name="view-category")
@click.argument("category")
def view_notes_by_category(category):
    """
    View notes by a specific category.

    Example:
    python main.py view-category "Personal"
    """
    result = note_app.view_notes_by_category(category)
    click.echo(result)
