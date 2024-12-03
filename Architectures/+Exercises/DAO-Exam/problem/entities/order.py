from abc import ABC, abstractmethod
from typing import List
from .product import Product

class Order(ABC):

    @abstractmethod
    def is_credit_card_number_valid(self, user_input: str) -> bool:
        pass

    @abstractmethod
    def set_credit_card_number(self, user_input: str) -> None:
        pass

    @abstractmethod
    def set_products(self, products: List[Product]) -> None:
        pass

    @abstractmethod
    def set_customer_id(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def get_customer_id(self) -> int:
        pass