# Model View Controller Pattern

# Model
class Task:
    def __init__(self, description: str) -> None:
        self.description = description

class TaskModel:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_task_list(self):
        return self.tasks

# View
class TaskView:
    def show_tasks(self, tasks):
        print("Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.description}")
        print()


# Controller
class TaskController:
    def __init__(self, model: TaskModel, view: TaskView) -> None:
        self.model = model
        self.view = view

    def add_task(self, description: str) -> None:
        task = Task(description)
        self.model.add_task(task)

    def show_task_list(self):
        tasks = self.model.get_task_list()
        self.view.show_tasks(tasks)



def main():
    tarea_model = TaskModel()
    tarea_view = TaskView()
    
    tarea_controller = TaskController(tarea_model, tarea_view)

    tarea_controller.add_task("Buy Milk")
    tarea_controller.add_task("Study Design Patterns")

    tarea_controller.show_task_list()

if __name__ == "__main__":
    main()