#Factory Pattern

from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass


class ProductA(Product):

    def get_name(self) -> str:
        return 'Product A'
    
class ProductB(Product):

    def get_name(self) -> str:
        return 'Product B'
    

class ProductFactory:

    products = {
        'A': ProductA(),
        'B': ProductB(),
    }

    @staticmethod
    def create_product(type: str) -> Product:
        product_class = ProductFactory.products.get(type) 
        
        if product_class is not None:
            return product_class
        else:
            raise Exception(f"Product type {type} not found")
        

if __name__ == '__main__':

    product_a = ProductFactory.create_product('A')
    product_b = ProductFactory.create_product('B')

    print(product_a.get_name())
    print(product_b.get_name())
