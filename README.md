# Project Title

## Description
 It allows users to add, view, search, update, delete, and categorize notes. This is ideal fo rdevelopers,students, and professionals who prefer a terminal based workflow
 for organizing tasks. 
## Features

- Add note with a title, content, and category
- View notes by catehgory or search by keyword
- Update and delete notes.

## Installation
1.  Clone the repository:
	```bash
	gh repo Clone your-username/python-notetaking-cli
	cd python-note-taking -cli
        ```
2. Create a virtual enviornment: 
  
   python -m venv
   source venv/bin/activate  #windows : venv\scripts\activate

3.  Install dependencies: 
    
    pip install -r requirements.txt

## Usage
- Add a Note:
   ```bash
   python main.py add "Title" "Content" "Category"
   ```
- View Notes:
  python main.py view

- Search Notes:
 
python main.py  "keyword"

- Category:
 python main.py view_category "Category"
## Testing
 manual testing or pytest or unittest can be used

## FAQ
   This is for the course for students to learn

## Contributing

We welcome contributions! Fork this repository, create a feature branch, and open a pull request.

## License
  We will address the licence later when we discuss things

