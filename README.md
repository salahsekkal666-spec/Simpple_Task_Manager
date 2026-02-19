# Simple Task Manager

Mini Project – PhD Programming Course  
University: Mohamed Kheider – Biskra  
Academic Year: 2025/2026  
Author: Salah Sekkal  

---

## Overview

This project is a simple Command-Line Task Manager written in Python.

It allows the user to:

- Add tasks
- View tasks
- Mark tasks as done
- Save tasks using JSON
- Load tasks automatically when the program starts

---

## Project Files

This project contains the following files:

- tasks.py → Main Python program  
- tasks.json → File used to store tasks  
- README.md → Project documentation  
- LICENSE → Project license  
- .gitignore → Git ignore configuration  

---

## Requirements

Python 3 must be installed on your computer.

You can check using:

```
python --version
```

---

## How to Run the Program

Step 1: Download or clone the repository

Step 2: Open terminal in the project folder

Step 3: Run the following command:

```
python tasks.py
```

---

## Program Menu

When you run the program, the following menu will appear:

```
===== TASK MANAGER =====

1. Add task
2. View tasks
3. Mark task as done
4. Exit
```

---

## Example Usage

Example:

```
Choose option: 1
Enter new task: Study Python
Task added successfully.
```

Display tasks:

```
Choose option: 2

Task List:

1. Study Python ❌
```

Mark task as done:

```
Choose option: 3

Enter task number: 1

Task marked as done.
```

Display again:

```
Choose option: 2

Task List:

1. Study Python ✔️
```

---

## Example of tasks.json file

```
[
    {
        "task": "Study Python",
        "done": true
    }
]
```

---

## Concepts Used

This project demonstrates:

- Python functions
- JSON file handling
- File saving and loading
- Error handling
- Command Line Interface (CLI)
- Git and GitHub version control

---

## GitHub

This project is uploaded to GitHub.

GitHub is used for:

- Saving the project online
- Tracking changes using commits
- Managing project versions

---

## Author

Salah Sekkal "and" boumedienne bouti 
PhD Student  
University of Mohamed Kheider – Biskra
