from abc import ABC, abstractmethod

class Product(ABC):

    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @id.setter
    @abstractmethod
    def id(self, value: int) -> None:
        pass

    @property
    @abstractmethod
    def product_name(self) -> str:
        pass

    @product_name.setter
    @abstractmethod
    def product_name(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def category_name(self) -> str:
        pass

    @category_name.setter
    @abstractmethod
    def category_name(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass