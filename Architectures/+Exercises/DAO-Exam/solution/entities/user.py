from abc import ABC, abstractmethod

class User(ABC):

    @property
    @abstractmethod
    def user_id(self) -> int:
        pass

    @user_id.setter
    @abstractmethod
    def user_id(self, value: int) -> None:
        pass

    @property
    @abstractmethod
    def first_name(self) -> str:
        pass

    @first_name.setter
    @abstractmethod
    def first_name(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def last_name(self) -> str:
        pass

    @last_name.setter
    @abstractmethod
    def last_name(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def password(self) -> str:
        pass

    @password.setter
    @abstractmethod
    def password(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def email(self) -> str:
        pass

    @email.setter
    @abstractmethod
    def email(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def money(self) -> float:
        pass

    @money.setter
    @abstractmethod
    def money(self, value: float) -> None:
        pass

    @property
    @abstractmethod
    def credit_card(self) -> str:
        pass

    @credit_card.setter
    @abstractmethod
    def credit_card(self, value: str) -> None:
        pass