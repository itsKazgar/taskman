# TaskMan 📋

A simple command-line task manager built in Python. Add, list, complete, and delete tasks — all saved locally so your data persists between sessions.

Built as a portfolio project to demonstrate Python fundamentals, CLI design, and file I/O.

---

## Features

- Add tasks with priority levels (high, medium, low) and optional due dates
- List all pending tasks or include completed ones
- Mark tasks as done or delete them
- Data saved to a local `tasks.json` file — no database needed
- Friendly error messages and input validation

---

## Requirements

- Python 3.6 or higher
- No external libraries required

---

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/taskman.git

# Navigate into the folder
cd taskman
```

---

## Usage

```bash
# Show help
python3 taskman.py help

# Add a task
python3 taskman.py add "Buy groceries" high "2024-12-01"
python3 taskman.py add "Read a book" low

# List pending tasks
python3 taskman.py list

# List all tasks including completed
python3 taskman.py list --all

# Mark a task as done (use the ID shown in the list)
python3 taskman.py done 1

# Delete a task
python3 taskman.py delete 2
```

---

## Example Output

```
=======================================================
           📋  YOUR TASKS
=======================================================

  PENDING:

  [1] 🔴 Buy groceries
       Priority : High
       Due      : 2024-12-01
       Added    : 2024-11-20 14:32

  [2] 🟢 Read a book
       Priority : Low
       Due      : No due date
       Added    : 2024-11-20 14:33

=======================================================
  Total: 2 pending | 0 done
=======================================================
```

---

## Project Structure

```
taskman/
├── taskman.py      # Main application
├── tasks.json      # Auto-generated when you add your first task
├── README.md       # This file
├── .gitignore      # Files excluded from Git
└── LICENSE         # MIT License
```

---

## What I Learned

- Parsing command-line arguments with `sys.argv`
- Reading and writing JSON files for data persistence
- Structuring a Python project with clean, single-purpose functions
- Input validation and user-friendly error handling
- Writing docstrings and maintaining readable code

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
