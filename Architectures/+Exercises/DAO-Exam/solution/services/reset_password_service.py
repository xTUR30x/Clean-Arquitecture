from abc import ABC, abstractmethod
from ..entities.user import User

class ResetPasswordService(ABC):

    @abstractmethod
    def reset_password_for_user(self, user: User) -> None:
        pass