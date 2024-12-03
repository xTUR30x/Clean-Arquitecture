from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def get_first_name(self) -> str:
        pass

    @abstractmethod
    def get_last_name(self) -> str:
        pass

    @abstractmethod
    def get_password(self) -> str:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def set_password(self, new_password: str) -> None:
        pass

    @abstractmethod
    def set_email(self, new_email: str) -> None:
        pass