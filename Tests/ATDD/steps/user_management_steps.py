from behave import given, when, then

class UserManager:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if not password:
            return False, "Password is required."
        
        if username in self.users:
            return False, "Username is already taken."

        self.users[username] = password
        return True, "Account created successfully."
    

@given('I am on the registration page')
def step_impl(context):
    context.user_manager = UserManager()

@when('I enter a valid username and password')
def step_impl(context):
    context.result, context.message = context.user_manager.register('new_user', 'secure_password')

@then('my account should be created and I should be redirected to the homepage')
def step_impl(context):
    assert context.result is True
    assert context.message == "Account created successfully."

@when('I enter a username that already exists')
def step_impl(context):
    context.user_manager.register("existing_user", "password123") 
    context.result, context.message = context.user_manager.register("existing_user", "another_password")

@then('I should see an error message indicating that the username is already taken')
def step_impl(context):
    assert context.result is False
    assert context.message == "Username is already taken."

@when('I do not enter a password')
def step_impl(context):
    context.result, context.message = context.user_manager.register("new_user_without_password", "")

@then('I should see an error message indicating that the password is required')
def step_impl(context):
    assert context.result is False
    assert context.message == "Password is required."