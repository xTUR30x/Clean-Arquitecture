#Visitor Pattern

from __future__ import annotations
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def tax_food(self, food: Food) -> str:
        pass

    @abstractmethod
    def tax_clothing(self, cloth: Cloth) -> str:
        pass

class Product(ABC):
    def __init__(self, price: float) -> None:
        self.price = price

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

    def __str__(self) -> str:
        return f"{self.price}"

class Food(Product):
    def __init__(self, price: float) -> None:
        super().__init__(price)

    def accept(self, visitor: Visitor):
        return visitor.tax_food(self)
    

class Cloth(Product):
    def __init__(self, price: float) -> None:
        super().__init__(price)

    def accept(self, visitor: Visitor):
        return visitor.tax_clothing(self)
    

class TaxVisitor(Visitor):
    def tax_food(self, food: Food) -> str:
        tax = food.price * 0.05
        return f"Food Tax ${tax:.2f}"
    
    def tax_clothing(self, cloth: Cloth) -> str:
        tax = cloth.price * 0.10
        return f"Clothing Tax ${tax:.2f}"
    
if __name__ == "__main__":
    apple = Food(10)
    shirt = Cloth(20)

    tax_visitor = TaxVisitor()

    print(apple.accept(tax_visitor))
    print(shirt.accept(tax_visitor))