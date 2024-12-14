import json
from datetime import date
import os

def create_file():
    file_path = "C:\\VScode\\gettingstarted\\python test files\\new_file.json"
    
    if os.path.exists(file_path):
        print(f"The file '{file_path}' already exists.")
    else:
        with open(file_path, "w") as file:
            json.dump({}, file)  # Create an empty JSON object
        print(f"'{file_path}' created successfully!")
        

def add_task():
    try:
        with open("C:\\VScode\\gettingstarted\\python test files\\new_file.json", "r") as file:
            existing_tasks = json.load(file) #to check if tasks exist
    except (FileNotFoundError, json.JSONDecodeError):
        existing_tasks = {} #if no tasks exist

    entries = int(input("Input the number of Tasks that you would like to add: "))

    for i in range(entries):

        task_description = input(f"Enter description for task {i+1}: ")
        due_date = input("Enter due date for the task (optional, press ENTER to SKIP): ")
        date_created = str(date.today())
        date_modified = date_created

        task_id = len(existing_tasks) + 1 #if n tasks exists, new task id = n+1
        existing_tasks[task_id] = {
            "description": task_description,
            "due date": due_date if due_date else None,
            "date created": date_created,
            "date modified": date_modified
        }

    with open("C:\\VScode\\gettingstarted\\python test files\\new_file.json", "w") as file:
        json.dump(existing_tasks, file, indent=4) #writing the old and new tasks in json

    print("-----Successfully added tasks!-----")


def edit_task():
    print("Editing tasks is not yet implemented.")


def delete_task():
    print("Deleting tasks is not yet implemented.")


def view():
    try:
        with open("C:\\VScode\\gettingstarted\\python test files\\new_file.json", "r") as file:
            tasks = json.load(file)
        print(json.dumps(tasks, indent=4))
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks to display.")

print("______Welcome to the TASK MANAGER!_____")


print(
    f"What would you like to do?"
    f"\n1. Write a new task"
    f"\n2. Delete a task"
    f"\n3. Edit an existing task"
    f"\n4. View all tasks"
    f"\n5. Create new file"
)

user_action = input("--->")

if user_action == "1":
    add_task()

elif user_action == "2":
    delete_task()

elif user_action == "3":
    edit_task()

elif user_action == "4":
    view()

elif user_action == "5":
    create_file()


else:
    print("Please select (1/2/3/4/5) only!")

