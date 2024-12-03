from abc import ABC, abstractmethod
from typing import List
from ..dtos.user_dto import UserDTO

class UserDAO(ABC):

    @abstractmethod
    def get_users(self) -> List[UserDTO]:
        pass

    @abstractmethod
    def save_user(self) -> bool:
        pass

    @abstractmethod
    def get_user_by_email(self) -> UserDTO:
        pass

    @abstractmethod
    def get_user_by_id(self) -> UserDTO:
        pass
