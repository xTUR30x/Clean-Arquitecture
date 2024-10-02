from user_security_manager import *

class UserRegistration:

    def __init__(self) -> None:
        self.user_registrationManager = UserSecurityManager()

    def register_user(self, username:str, password:str) -> bool:

        if self.user_registrationManager._validate_username(username):
            if self.user_registrationManager._validate_password(password):
                print("User register succesfully")
                return True
            else:
                print("Invalid password")
                return False
        else:
            print("Invalid username")
            return False