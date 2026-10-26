
tasks = []
task_id = 1

while True:
    print("\n===== TODO APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ")

        task = {
            "ID": task_id,
            "Task": task_name,
            "Status": "Pending"
        }

        tasks.append(task)
        print("Task added successfully!")
        task_id += 1

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n===== TASK LIST =====")
            for task in tasks:
                print("ID:", task["ID"])
                print("Task:", task["Task"])
                print("Status:", task["Status"])
                print()

    elif choice == "3":
        update_id = int(input("Enter task ID to update: "))
        found = False

        for task in tasks:
            if task["ID"] == update_id:
                new_name = input("Enter new task name: ")
                task["Task"] = new_name
                print("Task updated successfully!")
                found = True
                break

        if not found:
            print("Task ID not found.")

    elif choice == "4":
        complete_id = int(input("Enter task ID to complete: "))
        found = False

        for task in tasks:
            if task["ID"] == complete_id:
                task["Status"] = "Completed"
                print("Task marked as completed!")
                found = True
                break

        if not found:
            print("Task ID not found.")

    elif choice == "5":
        delete_id = int(input("Enter task ID to delete: "))
        found = False

        for task in tasks:
            if task["ID"] == delete_id:
                tasks.remove(task)
                print("Task deleted successfully!")
                found = True
                break

        if not found:
            print("Task ID not found.")

    elif choice == "6":
        print("Thank you for using the To-Do Application!")
        break

    else:
        print("Invalid choice. Please try again.")
