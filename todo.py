class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: '{task}'")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Your tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: '{removed_task}'")
        else:
            print("Invalid task number.")

    def show_menu(self):
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                if self.tasks:
                    task_number = int(input("Enter the task number to remove: "))
                    self.remove_task(task_number)
            elif choice == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if _name_ == "_main_":
    todo_list = ToDoList()
    todo_list.run()