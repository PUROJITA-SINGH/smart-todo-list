import json
from datetime import datetime
import os

# Initialize tasks list
tasks = []

def load_tasks():
    """Load tasks from tasks.json if it exists."""
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading tasks file. Starting with empty list.")
            return []
    return []

def save_tasks():
    """Save tasks to tasks.json."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a single task."""
    description = input("Enter task description: ")
    priority = input("Enter priority (High, Medium, Low): ").capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority! Using Medium.")
        priority = "Medium"
    due_date = input("Enter due date (YYYY-MM-DD, e.g., 2025-07-25): ")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Using today's date.")
        due_date = datetime.now().strftime("%Y-%m-%d")
    
    task = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks()
    print(f"Added task: {description} (Priority: {priority}, Due: {due_date})")

def add_multiple_tasks():
    """Add multiple tasks in one session."""
    print("\n=== Add Multiple Tasks ===")
    print("Enter tasks one by one. Type 'done' when finished.")
    
    while True:
        description = input("\nEnter task description (or 'done' to finish): ")
        if description.lower() == 'done':
            print("Finished adding tasks.")
            break
        priority = input("Enter priority (High, Medium, Low): ").capitalize()
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority! Using Medium.")
            priority = "Medium"
        due_date = input("Enter due date (YYYY-MM-DD, e.g., 2025-07-25): ")
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Using today's date.")
            due_date = datetime.now().strftime("%Y-%m-%d")
        
        task = {
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "status": "Pending"
        }
        tasks.append(task)
        save_tasks()
        print(f"Added task: {description} (Priority: {priority}, Due: {due_date})")

def view_tasks():
    """View tasks sorted by priority or due date."""
    if not tasks:
        print("No tasks to display.")
        return
    sort_by = input("Sort by (1: Priority, 2: Due Date): ")
    if sort_by == "1":
        sorted_tasks = sorted(tasks, key=lambda x: (["High", "Medium", "Low"].index(x["priority"]), x["due_date"]))
    else:
        sorted_tasks = sorted(tasks, key=lambda x: (x["due_date"], ["High", "Medium", "Low"].index(x["priority"])))
    
    print("\n=== Task List ===")
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. {task['description']} | Priority: {task['priority']} | Due: {task['due_date']} | Status: {task['status']}")

def mark_task_status():
    """Mark a task as completed or pending."""
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to update status: ")) - 1
        if 0 <= index < len(tasks):
            status = input("Set status (Completed, Pending): ").capitalize()
            if status in ["Completed", "Pending"]:
                tasks[index]["status"] = status
                save_tasks()
                print(f"Updated task '{tasks[index]['description']}' to {status}")
            else:
                print("Invalid status! Use 'Completed' or 'Pending'.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Enter a number.")

def main():
    """Main function to run the to-do list."""
    global tasks
    tasks = load_tasks()
    
    while True:
        print("\n=== Smart To-Do List ===")
        print("1. Add Single Task")
        print("2. Add Multiple Tasks")
        print("3. View Tasks")
        print("4. Mark Task Status")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            add_multiple_tasks()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            mark_task_status()
        elif choice == "5":
            print("Thank you for using the Smart To-Do List!")
            break
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()
