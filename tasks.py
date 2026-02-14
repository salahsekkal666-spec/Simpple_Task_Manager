import json
import os

FILE_NAME = "tasks.json"
##
print("JSON FILE PATH:", os.path.abspath(FILE_NAME))


# -----------------------
# -----------------------
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
            return tasks
    except:
        return []


# -----------------------
# -----------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------
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
# -----------------------
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nTask List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['task']} {status}")


# -----------------------
tasks = load_tasks()
list_tasks(tasks)
#########---
def mark_done(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark as done: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")
#####################
tasks = load_tasks()
add_task(tasks)        # 
list_tasks(tasks)      # 
mark_done(tasks)       # 
list_tasks(tasks)      #


