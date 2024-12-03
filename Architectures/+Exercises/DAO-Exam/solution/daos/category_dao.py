from abc import ABC, abstractmethod
from ..dtos.category_dto import CategoryDTO

class CategoryDAO(ABC):

    @abstractmethod
    def get_category_by_id(self) -> CategoryDTO:
        pass
