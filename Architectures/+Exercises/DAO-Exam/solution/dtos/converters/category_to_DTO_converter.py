from ..category_dto import CategoryDTO

class ProductToProductDTOConverter:

    def convert_category_name_to_dto(self, category_name: str) -> CategoryDTO:
        category_dto = CategoryDTO()
        category_dto.name = category_name
        return category_dto