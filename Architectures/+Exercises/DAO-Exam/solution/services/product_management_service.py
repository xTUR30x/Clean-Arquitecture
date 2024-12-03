from abc import ABC, abstractmethod
from typing import List
from ..entities.product import Product

class ProductManagementService(ABC):

    @abstractmethod
    def get_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id_to_add_to_cart: int) -> Product:
        pass