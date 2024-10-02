class UserSecurityManager:

    def _validate_username(self, username:str) -> bool:
        return len(username) >= 5 

    def _validate_password(self, password:str) -> bool:
        return len(password) >= 8