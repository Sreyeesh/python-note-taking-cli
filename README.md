# Python Note-Taking CLI App

A command-line application for managing notes, allowing users to add, view, search, update, delete, and categorize notes.

## Features
- Add notes with title, content, and category
- View notes by category or search by keyword
- Update and delete notes

## Installation
```bash
gh repo clone your-username/python-note-taking-cli
cd python-note-taking-cli
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt


Usage
Add a Note: python main.py add "Title" "Content" "Category"
View Notes: python main.py view
Search Notes: python main.py search "keyword"
View Notes by Category: python main.py view_category "category"

## Testing NoteApp

- We use `pytest` for testing the application.
- The `pytest.ini` file ensures the project root is included in Python’s module search path, simplifying test execution.
- To run tests locally:
  ```bash
  pytest

## CI/CD Pipeline

- The GitHub Actions workflow (`python-ci.yml`) ensures automated testing on every push to the `main` branch.
- Key updates:
  - Added `pytest.ini` for simplified test configuration.
  - Verified that the workflow successfully passes all tests.
