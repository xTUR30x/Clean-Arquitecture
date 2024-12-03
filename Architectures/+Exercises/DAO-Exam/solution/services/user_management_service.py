from abc import ABC, abstractmethod
from typing import List
from ..entities.user import User

class UserManagementService(ABC):

    @abstractmethod
    def register_user(self, user: User) -> str:
        pass

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

    @abstractmethod
    def get_user_by_email(self, user_email: str) -> User:
        pass