# to_do_list_cli.py

import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks found.\n")
        return
    print("\n📝 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")
    print()

def add_task(tasks):
    title = input("Enter a new task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Task added!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as complete!")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("🗑️ Task deleted!")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number!")

def main():
    tasks = load_tasks()
    while True:
        print("\n==== TO-DO LIST ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again!")

if __name__ == "__main__":
    main()
