from typing import List
from ..purchase_dto import PurchaseDTO
from ...entities.purchase import Purchase
from .user_to_DTO_converter import UserToUserDTOConverter
from .product_to_DTO_converter import ProductToProductDTOConverter

class PurchaseToPurchaseDTOConverter:

    def __init__(self) -> None:
        self._product_converter = ProductToProductDTOConverter()
        self._user_converter = UserToUserDTOConverter()

    def convert_purchase_to_dto(self, purchase: Purchase) -> PurchaseDTO:
        purchaseDTO = PurchaseDTO()
        purchaseDTO.products = self._product_converter(purchase.products)
        purchaseDTO.user = self._user_converter(purchase.user)

    def convert_dto_to_purchase(self, purchaseDTO: PurchaseDTO) -> Purchase:
        purchase = Purchase()
        purchase.products = self._product_converter(purchaseDTO.products)
        purchase.user = self._user_converter(purchaseDTO.user)


    def convert_all_purchases_to_DTOs(self, purchases: List[Purchase]) -> List[PurchaseDTO]:
        purchaseDTos = []

        for purchase in purchases:
            purchaseDTos.append(self.convert_purchase_to_dto(purchase))

        return purchaseDTos
    
    def convert_all_dtos_to_purchases(self, purchaseDTOs: List[PurchaseDTO]) -> List[Purchase]:
        purchases = []

        for dto in purchaseDTOs:
            purchases.append(self.convert_dto_to_purchase(dto))

        return purchases