from behave import given, when, then

class TaskManager:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, title: str, description: str) -> None:
        if not title:
            print("Error, title is required")
            return False
        
        self.tasks.append({"Title": title, "description": description})
        return True
    

@when('I am on the task page')
def step_impl(context):
    context.result = context.task_manager.add_task("Buy groceries", "Milk, Bread, Eggs")

@then('The task should be added to the task list')
def step_impl(context):
    assert context.result is True
    assert len(context.task_manager.tasks) == 1
    assert context.task_manager.tasks[0]["Title"] == "Buy groceries"

@when('I enter an empty title')
def step_impl(context):
    context.result = context.task_manager.add_task("", "Some description")

@then('I should see an error message indicating that the title is required')
def step_impl(context):
    assert context.result is False
    assert context.task_manager.error_message == "Title is required."