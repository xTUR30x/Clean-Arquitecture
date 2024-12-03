from abc import ABC, abstractmethod
from typing import List
from ..dtos.product_dto import ProductDTO

class ProductDAO(ABC):

    @abstractmethod
    def get_products(self) -> List[ProductDTO]:
        pass

    @abstractmethod
    def get_product_by_id(self) -> ProductDTO:
        pass
