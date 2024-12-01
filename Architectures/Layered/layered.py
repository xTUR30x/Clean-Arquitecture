# Layered Architecture
import sqlite3

# Model
class Task:
    def __init__(self, description):
        self.description = description

# Presentation
class TaskView:
    def show_tasks(self, tasks):
        print("Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.description}")
        print()

# Business Logic
class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, description):
        new_task = Task(description)
        self.repository.add_task(new_task)

    def get_tasks(self):
        return self.repository.list_tasks()

# Persistence
class TaskRepository:
    def __init__(self, data_access):
        self.data_access = data_access

    def add_task(self, task):
        self.data_access.add_task(task)

    def list_tasks(self):
        return self.data_access.list_tasks()

# Data
class TaskDataAccess:
    def __init__(self, db_name='tasks.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL
            )
            """)

    def add_task(self, task):
        with self.connection:
            self.connection.execute("INSERT INTO tasks (description) VALUES (?)", (task.description,))

    def list_tasks(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT description FROM tasks")
        return [Task(row[0]) for row in cursor.fetchall()]

def main():
    # Create instances
    data_access = TaskDataAccess()
    repository = TaskRepository(data_access)
    service = TaskService(repository)
    view = TaskView()

    # Add tasks
    service.create_task("Buy milk")
    service.create_task("Study design patterns")

    # List tasks
    tasks = service.get_tasks()
    view.show_tasks(tasks)

if __name__ == "__main__":
    main()