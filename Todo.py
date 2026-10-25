def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def todo_app():
    tasks = []
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\n--- YOUR TASKS ---")
                for index, task in enumerate(tasks, start=1):
                    status = "✓" if task['completed'] else " "
                    print(f"{index}. [{status}] {task['title']}")
                    
        elif choice == '2':
            title = input("\nEnter the task description: ").strip()
            if title:
                tasks.append({'title': title, 'completed': False})
                print(f"Added task: '{title}'")
            else:
                print("Task cannot be empty!")
                
        elif choice == '3':
            if not tasks:
                print("\nNo tasks to mark as completed.")
                continue
            try:
                task_num = int(input("\nEnter the task number to mark completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['completed'] = True
                    print(f"Marked task {task_num} as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '4':
            if not tasks:
                print("\nNo tasks to delete.")
                continue
            try:
                task_num = int(input("\nEnter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Deleted task: '{removed['title']}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")

if __name__ == "__main__":
    todo_app()
