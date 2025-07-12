def print_menu():
    print('To List Menu:')
    print('1. View Tasks')
    print('2. Add a task')
    print('3. Remove tasks')

def get_choice():
    while True:
        choice = input('Enter your choice: ')
        valid_choices = ['1', '2', '3', '4']
        if choice not in valid_choices:
            print('Invalid choice. Please enter a number between 1 and 3.')
            continue
        else:
            return choice

def display_tasks(tasks):
    print("")
    if not tasks:
        print('No tasks found.')
        return

    print('Tasks:')
    for index,task in enumerate(tasks, start=1):
        print(f'{index}. {task}')
    print("")

def add_task(tasks):
    while True:
        task = input('Enter the task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print('Task cannot be empty. Please enter a valid task.')
    print("")

def remove_task(tasks):
    display_tasks(tasks)

    while True:
        try:
            task_number = int(input('Enter the number of the task to remove: '))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid input. Please enter a number.')

    print("")
            

def main():
    tasks = []

    while True:
        print_menu()
        choice = get_choice()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        else:
            break

if __name__ == '__main__':
    main()