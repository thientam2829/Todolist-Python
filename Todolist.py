def Add():
    print('\n--- Add Task ---')
    add_task = input('Please write the task: ')
    if add_task not in Tasks:
        Tasks.append(add_task)
        formatted_tasks = ', '.join(f"{task}" for task in Tasks)
        print('Last task added:', add_task)
        print("List of tasks after addition:", formatted_tasks)
    else:
        print('Task is already found in the list of tasks.')

def Edit():
    print("\n--- Edit Tasks ---")
    formatted_tasks = ', '.join(f"{task}" for task in Tasks)
    print('Tasks:', formatted_tasks)
    edit_task = input('Wich task do you want to edit? ').lower()
    if edit_task in Tasks:
        edited_task = input('Please write your new task: ').lower()
        index = Tasks.index(edit_task)
        Tasks[index] = edited_task
        formatted_tasks = ', '.join(f"{task}" for task in Tasks)
        print('List of tasks after edition:', formatted_tasks)
    else:
        print('Task not found in the list of tasks.')

def CompletedTask():
    print("\n--- Completed Task ---")
    formatted_tasks = ', '.join(f"{task}" for task in Tasks)
    print('Tasks:', formatted_tasks)
    completed_task = input('Which task do you want to mark as completed? ').lower()
    if completed_task in Tasks:
        Tasks.remove(completed_task)
        Completed.append(completed_task)
        formatted_completed_tasks = ', '.join(f"{complete}" for complete in Completed)
        print('Last task completed:', completed_task)
        print('List of uncompleted tasks:', formatted_tasks)
        print('List of completed tasks:', formatted_completed_tasks)
    else:
        print('Task not found in the list of tasks.')

def Delete():
    print("\n--- Delete Task ---")
    formatted_tasks = ', '.join(f"{task}" for task in Tasks)
    print('Tasks:', formatted_tasks)
    delete_task = input('Wich task do you want to delete? ').lower()
    if delete_task in Tasks:
        Tasks.remove(delete_task)
        print('Last task deleted:', delete_task)
        print('List of tasks after deletion:', formatted_tasks)
    else:
        print('Task not found in the list of tasks.')

def View():
    print("\n--- View Tasks ---")
    formatted_tasks = ', '.join(f"{task}" for task in Tasks)
    print('Tasks:', formatted_tasks)
Tasks = []
Completed = []
while True:
    print('\n------ TO-DO-LIST ------')
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Completed Task")
    print("4. Delete Task")
    print("5. View Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        Add()
    if choice == '2':
        Edit()
    elif choice == '3':
        CompletedTask()
    elif choice == '4':
        Delete()
    elif choice == '5':
        View()
    elif choice == '6':
        print("You choose Exit")
        quit()
    else:
        print("Invalid choice!")