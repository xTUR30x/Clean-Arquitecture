from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def get_product_name(self) -> str:
        pass

    @abstractmethod
    def get_category_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def set_price(self, price: float) -> None:
        pass