import json
import os

FILE_NAME = "tasks.json"


# -----------------------
# Load tasks
# Official reference:
# https://docs.python.org/3/library/json.html
# -----------------------
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# -----------------------
# Save tasks
# -----------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------
# Add task
# -----------------------
def add_task(tasks):

    task = input("Enter new task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
        return

    tasks.append({"task": task, "done": False})

    save_tasks(tasks)

    print("Task added successfully.")


# -----------------------
# List tasks
# -----------------------
def list_tasks(tasks):

    if not tasks:
        print("No tasks found.")
        return

    print("\nTask List:")

    for i, task in enumerate(tasks, 1):

        status = "✔️" if task["done"] else "❌"

        print(f"{i}. {task['task']} {status}")


# -----------------------
# Mark done
# -----------------------
def mark_done(tasks):

    list_tasks(tasks)

    if not tasks:
        return

    try:

        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):

            tasks[number - 1]["done"] = True

            save_tasks(tasks)

            print("Task marked as done.")

        else:

            print("Invalid task number.")

    except ValueError:

        print("Invalid input.")


# -----------------------
# MENU
# Official reference:
# https://docs.python.org/3/library/functions.html#input
# -----------------------
def menu():

    tasks = load_tasks()

    while True:

        print("\n===== TASK MANAGER =====")

        print("1. Add task")

        print("2. View tasks")

        print("3. Mark task as done")

        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":

            add_task(tasks)

        elif choice == "2":

            list_tasks(tasks)

        elif choice == "3":

            mark_done(tasks)

        elif choice == "4":

            print("Goodbye!")

            break

        else:

            print("Invalid choice.")


# -----------------------
# Run program
# -----------------------
menu()
