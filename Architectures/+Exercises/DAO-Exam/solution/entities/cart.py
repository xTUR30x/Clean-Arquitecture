from abc import ABC, abstractmethod
from typing import List
from .product import Product

class Cart(ABC):

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_products(self) -> List[Product]:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass