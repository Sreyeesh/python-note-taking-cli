

# **Note-Taking CLI**

A lightweight, efficient, and user-friendly command-line interface (CLI) application for managing your notes. The app supports note categorization, tagging, and persistent storage, offering a streamlined and productive workflow for users.

---

## **Features**
- **Create Notes:** Add notes with titles, content, categories, and optional tags.
- **View Notes:** List all notes with pagination support.
- **Delete Notes:** Remove notes by title.
- **Persistent Storage:** Saves notes in a JSON file located in the user's home directory for easy access and privacy.
- **Robust Codebase:** Follows best practices for maintainable and reusable code.
- **Linting and Formatting:** Integrated with tools like `flake8` and `black` to ensure clean, readable code.

---

## **Repository Structure**

Below is the organized structure of the repository, designed for clarity and professionalism.

```plaintext
python-note-taking-cli/
│
├── app/                     # Application logic
│   ├── __init__.py          # Package initializer
│   ├── cli.py               # CLI commands
│   ├── main.py              # Application entry point
│   └── note_app.py          # Core note management functionality
│
├── tests/                   # Test suite
│   ├── __init__.py          # Test package initializer
│   ├── test_cli.py          # Tests for CLI commands
│   └── test_note_app.py     # Tests for the note management module
│
├── .github/                 # GitHub workflows
│   └── workflows/
│       └── python-package.yml  # CI/CD workflow for linting and testing
│
├── data/                    # Directory for persistent data
│   └── notes.json           # JSON file for storing notes (auto-generated)
│
├── dist/                    # Distribution files (generated during build)
│   ├── note_taking_cli-1.0.0-py3-none-any.whl
│   └── note_taking_cli-1.0.0.tar.gz
│
├── .gitignore               # Git ignore file for untracked files
├── .flake8                  # Configuration file for flake8
├── pytest.ini               # Configuration file for pytest
├── README.md                # Project documentation (you are here)
├── requirements.txt         # List of dependencies
├── setup.py                 # Setup script for packaging and installation
└── LICENSE                  # Project license
```

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/Sreyeesh/python-note-taking-cli.git
cd python-note-taking-cli
```

### **2. Create and Activate a Virtual Environment**
- On **Windows**:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Install the CLI Globally**
```bash
pip install .
```

---

## **Usage**

### **General Command Syntax**
```bash
note-cli [OPTIONS] COMMAND [ARGS]...
```

### **Available Commands**
1. **Add a Note**
   ```bash
   note-cli add "Title" "Content" --category "Category" --tags "tag1,tag2"
   ```
   Example:
   ```bash
   note-cli add "Meeting Notes" "Discuss Q4 strategy." --category "Work" --tags "urgent,team"
   ```
   **Output:**
   ```
   Note added: Meeting Notes - Discuss Q4 strategy. (Category: Work, Tags: urgent, team)
   ```

2. **List Notes**
   ```bash
   note-cli list
   ```
   **Output:**
   ```
   1. Title: Meeting Notes
      Content: Discuss Q4 strategy.
      Category: Work
      Tags: urgent, team
   Page 1 of 1.
   ```

3. **Delete a Note**
   ```bash
   note-cli delete "Title"
   ```
   Example:
   ```bash
   note-cli delete "Meeting Notes"
   ```
   **Output:**
   ```
   Note with title 'Meeting Notes' has been deleted.
   ```

---

## **Development and Contribution**

### **Run Tests**
Ensure all features work as expected:
```bash
pytest
```

### **Lint and Format Code**
Run `flake8` and `black` to ensure the code adheres to Python best practices:
```bash
flake8 app tests
black app tests
```

### **Building the Project**
To package the application for distribution:
```bash
python setup.py sdist bdist_wheel
```

---

## **Known Issues**
- **Notes not being saved:** Ensure you have write access to the directory `~/.note-cli/data/`.
- **Command not recognized:** Verify the installation and that `pip install .` was run globally.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

