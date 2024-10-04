from abc import ABC, abstractmethod

class CompositeInterface(ABC):

    def get_price(self):
        pass

class Product(CompositeInterface):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price
    
    def __str__(self):
        return f"{self.name}: ${self.price}"
    

class Box(CompositeInterface):
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product: CompositeInterface):
        self.products.append(product)

    def get_price(self):
        total_price = sum(product.get_price() for product in self.products)
        return total_price
    
    def __str__(self):
        return f"{self.name} (Total: ${self.get_price()})"


if __name__ == '__main__':
    box1 = Box("Box 1")
    box2 = Box("Box 2")
    product_a = Product("Producto A", 20)
    product_b = Product("Producto B", 100)

    box1.add_product(product_a)
    box1.add_product(product_b)
    
    box2.add_product(product_b)

    print(f"Precio total de Caja 1: ${box1.get_price()}")
    print(f"Precio total de Caja 2: ${box2.get_price()}")