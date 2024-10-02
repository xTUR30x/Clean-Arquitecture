#Single Responsability Ex

#Problem

class UserDataManager:
    
    def __init__(self, username:str, password:str) -> None:
        self.username = username
        self.password = password
        
    def register_user(self) -> None:
        if _validate_username(self.username) and _validate_password(self.password):
            print("User register succesfully")
        else:
            print("Invalid username or password")

    def login_user(self):
        if _validate_username(self.username) and _validate_password(self.password):
            print("User logged succesfully")
        else:
            print("Invalid username or password")

    
    def _validate_username(self, username:str) -> bool:
        return len(username) >= 5 

    def _validate_password(self, password:str) -> bool:
        return len(password) >= 8
