tasks = []    # make a empty list to store tasks

def show_tasks():   # function to display tasks
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):  # enumerate to get index and task
            print(f"{i}. {task}")

def add_task():     # function to add a task
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():   # function to remove a task
    show_tasks()
    if tasks:
        try:     # show tasks before removing
            idx = int(input("Enter task number to remove: "))
            if 1 <= idx <= len(tasks):
                removed = tasks.pop(idx - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        except ValueError:   # handle non-integer input
            print("Please enter a valid number.")

while True:   # main loop to run the program
    print("\n1. Show tasks\n2. Add task\n3. Remove task\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice.")