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
@click.option("--page", default=1, help="Page number to display")
@click.option("--limit", default=5, help="Number of notes per page")
def list_notes(page, limit):
    """
    List all notes with pagination.

    Example:
    python main.py list --page 1 --limit 5
    """
    result = note_app.view_notes(page=page, limit=limit)
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
@click.option("--category", default=None, help="Filter by category")
def search_notes(keyword, category):
    """
    Search for notes containing a specific keyword, optionally filtered by category.

    Example:
    python main.py search "milk"
    python main.py search "milk" --category "Personal"
    """
    result = note_app.search_notes(keyword, category)
    click.echo(result)



@cli.command(name="view-category")
@click.argument("category")
@click.option("--page", default=1, help="Page number to display")
@click.option("--limit", default=5, help="Number of notes per page")
def view_notes_by_category(category, page, limit):
    """View notes by a specific category with pagination."""
    result = note_app.view_notes_by_category(category, page=page, limit=limit)
    click.echo(result)

def test_list_with_pagination(runner):
    for i in range(10):
        runner.invoke(cli, ["add", f"Note {i+1}", f"Content {i+1}", "--category", "General"])
    result = runner.invoke(cli, ["list", "--page", "2", "--limit", "5"])
    assert "Page 2 of 2." in result.output

def test_view_category_with_pagination(runner):
    for i in range(10):
        runner.invoke(cli, ["add", f"Note {i+1}", f"Content {i+1}", "--category", "Work"])
    result = runner.invoke(cli, ["view-category", "Work", "--page", "2", "--limit", "5"])
    assert "Page 2 of 2." in result.output
