from .category_dto import CategoryDTO

class ProductDTO:

    #Getter y Setter para _id
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    #Getter y Setter para _name
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    #Getter y Setter para _precio
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        self._price = value

    #Getter y Setter para _category
    @property
    def category(self) -> CategoryDTO:
        return self._category
    
    @category.setter
    def category(self, value: CategoryDTO) -> None:
        self._category = value