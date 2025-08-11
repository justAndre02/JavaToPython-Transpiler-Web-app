# Unit test result: ✅ PASSED
from datetime import datetime

class Task:

    def __init__(self, description: str, priority: int):
        self.description = description
        self.priority = priority
        self.completed = False
        self.creation_date = datetime.now().strftime('%Y-%m-%d %H:%M')

    def get_description(self) -> str:
        return self.description

    def get_priority(self) -> int:
        return self.priority

    def is_completed(self) -> bool:
        return self.completed

    def set_completed(self, completed: bool) -> None:
        self.completed = completed

    def get_creation_date(self) -> str:
        return self.creation_date
    description: str
    completed: bool
    priority: int
    creationDate: str

    def __init__(self, description: str, priority: int) -> None:
        self.description = description
        self.completed = False
        self.priority = priority
        now = datetime.now()
        self.creationDate = now.strftime('%Y-%m-%d %H:%M')

    def get_description(self) -> str:
        return self.description

    def is_completed(self) -> bool:
        return self.completed

    def set_completed(self, completed: bool) -> None:
        self.completed = completed

    def get_priority(self) -> int:
        return self.priority

    def get_creation_date(self) -> str:
        return self.creationDate

class TaskManager:

    def __init__(self):
        self.tasks: list['Task'] = []

    def add_task(self, description: str, priority: int) -> None:
        new_task = Task(description, priority)
        self.tasks.append(new_task)
        print('Task added successfully!')

    def view_tasks(self) -> None:
        if not self.tasks:
            print('No tasks available.')
            return
        print('\n===== TASK LIST =====')
        for (i, task) in enumerate(self.tasks):
            status = '[COMPLETED]' if task.is_completed() else '[PENDING]'
            print(f'{i + 1}. {status} - {task.get_description()} (Priority: {task.get_priority()}) Created: {task.get_creation_date()}')
        print('=====================\n')

    def mark_task_as_complete(self, task_index: int) -> None:
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.set_completed(True)
            print('Task marked as complete!')
        else:
            print('Invalid task number.')

    def run(self) -> None:
        running = True
        print('Welcome to Task Manager!')
        while running:
            print('\nPlease select an option:')
            print('1. Add new task')
            print('2. View all tasks')
            print('3. Mark task as complete')
            print('4. Exit')
            try:
                choice = int(input('Your choice: '))
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            match choice:
                case 1:
                    description = input('Enter task description: ')
                    priority = int(input('Enter priority (1-5): '))
                    self.add_task(description, priority)
                case 2:
                    self.view_tasks()
                case 3:
                    self.view_tasks()
                    try:
                        task_num = int(input('Enter task number to mark as complete: '))
                        self.mark_task_as_complete(task_num - 1)
                    except ValueError:
                        print('Invalid task number input. Please enter a number.')
                    except IndexError:
                        print('Task number out of range.')
                case 4:
                    running = False
                    print('Thank you for using Task Manager!')
                case _:
                    print('Invalid option. Please try again.')

    @staticmethod
    def main(args: list[str]) -> None:
        manager = TaskManager()
        manager.run()
if __name__ == '__main__':
    TaskManager.main([])