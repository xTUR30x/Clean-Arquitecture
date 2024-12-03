from typing import List
from .user_dto import UserDTO
from .product_dto import ProductDTO

class PurchaseDTO:

    # Getter and Setter for id
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    # Getter and Setter for user
    @property
    def user(self) -> UserDTO:
        return self._user
    
    @user.setter
    def user(self, value: UserDTO) -> None:
        self._user = value

    # Getter and Setter for products
    @property
    def products(self) -> List[ProductDTO]:
        return self._products
    
    @products.setter
    def products(self, value: List[ProductDTO]) -> None:
        self._products = value