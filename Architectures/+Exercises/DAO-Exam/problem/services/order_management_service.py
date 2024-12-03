from abc import ABC, abstractmethod
from typing import List
from ..entities.order import Order

class OrderManagementService(ABC):

    @abstractmethod
    def add_order(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_orders_by_user_id(self, user_id: int) -> List[Order]:
        pass

    @abstractmethod
    def get_orders(self) -> List[Order]:
        pass