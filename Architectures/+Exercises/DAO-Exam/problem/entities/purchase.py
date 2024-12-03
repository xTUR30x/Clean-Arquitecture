from abc import ABC, abstractmethod
from .product import Product
from .user import User

class Purchase(ABC):

    @property
    @abstractmethod
    def user(self) -> User:
        pass

    @user.setter
    @abstractmethod
    def user(self, value: User) -> None:
        pass

    @property
    @abstractmethod
    def products(self) -> Product:
        pass

    @products.setter
    @abstractmethod
    def products(self, value: Product) -> None:
        pass