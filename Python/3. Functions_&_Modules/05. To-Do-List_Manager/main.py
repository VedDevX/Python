tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def display_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f'Task "{removed}" removed.')
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task description: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            display_tasks()
            try:
                index = int(input("Enter task number to remove: ")) - 1
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
