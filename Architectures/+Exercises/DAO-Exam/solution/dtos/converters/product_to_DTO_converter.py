from typing import List
from ...entities.product import Product
from ...dtos.product_dto import ProductDTO
from .category_to_DTO_converter import CategoryToCategoryDTOConverter

class ProductToProductDTOConverter:

    def __init__(self) -> None:
        self._category_converter = CategoryToCategoryDTOConverter()

    def convert_dto_to_product(self, productDto: ProductDTO) -> Product:
        product = Product()
        product.id = productDto.id
        product.name = productDto.name
        product.price = productDto.price
        product.category_name = productDto.category.name

        return product
    
    def convert_product_to_dto(self, product: Product) -> ProductDTO:
        productDTO = ProductDTO()
        productDTO.id = product.id
        productDTO.name = product.name
        productDTO.price = product.price
        productDTO.category = self._category_converter.convert_category_name_to_dto(product.category_name)

        return productDTO
    

    def convert_all_product_to_DTOs(self, products: List[Product]) -> List[ProductDTO]:
        productDTOs = []

        for product in products:
            productDTOs.append(self.convert_product_to_dto(product))

        return productDTOs
    
    def convert_all_dtos_to_product(self, productDTOs: List[ProductDTO]) -> List[Product]:
        products = []

        for dto in productDTOs:
            products.append(self.convert_dto_to_product(dto))

        return products