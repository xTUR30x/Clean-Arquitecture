from user_security_manager import *

class UserAuthentication:

    def __init__(self) -> None:
        self.security_user_manager = UserSecurityManager()

    def authenticate_user(self, username:str, password:str) -> bool:

        if self.security_user_manager._validate_username(username):
            if self.security_user_manager._validate_password(password):
                print("User logged succesfully")
                return True
            else:
                print("Invalid password")
                return False
        else:
            print("Invalid username")
            return False
