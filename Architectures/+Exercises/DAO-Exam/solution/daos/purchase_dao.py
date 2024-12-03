from abc import ABC, abstractmethod
from typing import List
from ..dtos.purchase_dto import PurchaseDTO

class PurchaseDAO(ABC):

    @abstractmethod
    def save_purchase(self, order: PurchaseDTO) -> bool:
        pass

    @abstractmethod
    def get_purchase_by_id(self, user_id: int) -> List[PurchaseDTO]:
        pass

    @abstractmethod
    def get_purchases(self) -> List[PurchaseDTO]:
        pass
