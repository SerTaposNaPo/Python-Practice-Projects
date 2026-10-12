import json
import os

if os.path.exists("task.json"):
    with open("task.json", "r") as file:
        task = json.load(file)
        print("Previous tasks loaded")
else:
    task = []

def view_task():
    task_number = 0
    for title in range(len(task)):
        task_number += 1
        if not task[title]["done"]:
            print(f"{task_number}.[ ] {task[title]['title']}")
        else:
            print(f"{task_number}.[x] {task[title]['title']}")


def add_task():
    new_task = input("Add Task : ")
    get_task = {"title": new_task, "done": False}
    task.append(get_task)



def complete_task():
    try:
        completed_task = int(input("No. of task to Complete: "))
        index = completed_task - 1
        if index >= 0 and index < len(task):
            task[index]["done"] = True
            print(f"Task #{completed_task} marked as complete!")
        else:
            print("Error: That task number does not exist!")
    except ValueError:
        print("Error: Please enter a valid number, not letters!")





while True:
    print("== MENU ===")
    print("1. View Task")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        view_task()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":

        with open("task.json", "w") as file:
            json.dump(task, file, indent=4)

        print("The program successfully exit")
        break
    else:
        print("Invalid input")
