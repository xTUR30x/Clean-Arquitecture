from abc import ABC, abstractmethod
from typing import Any, List

class Pizza:
    def __init__(self) -> None:
        self._sauce = None
        self._ingredients: List[str] = []

    @property
    def sauce(self) -> Any:
        return self._sauce
    
    @property
    def ingredients(self) -> List[str]:
        return self._ingredients
    
    def show_ingredients(self) -> None:
        print(f"Ingredientes: {', '.join(self._ingredients)}")

    def show_sauce(self) -> None:
        print(self._sauce)
    


class PizzaBuilder(ABC):
    """
    Interfaz del Builder que especifica métodos para crear partes del producto.
    """

    def __init__(self) -> None:
        self._pizza = Pizza()

    @abstractmethod
    def build(self) -> Pizza:
        pass

    def reset(self) -> None:
        self._pizza = Pizza()

    @abstractmethod
    def set_sauce(self) -> None:
        pass

    @abstractmethod
    def set_ingredients(self) -> None:
        pass


class MargheritaPizzaBuilder(PizzaBuilder):
    
    def set_ingredients(self) -> None:
        self._pizza._ingredients.append("Tomato")

    def set_sauce(self) -> None:
        self._pizza._sauce = "Margherita Sauce"


    def build(self) -> Pizza:
        product = self._pizza
        self.reset()
        return product


class NewYorkPizzaBuilder(PizzaBuilder):

    def set_ingredients(self) -> None:
        self._pizza._ingredients.append("Tomato")
        self._pizza._ingredients.append("Pepperoni")

    def set_sauce(self) -> None:
        self._pizza._sauce = "New York Sauce"

    def build(self) -> Pizza:
        product = self._pizza
        self.reset()
        return product


class PizzaDirector:
    """
    La clase controladora de los builders, en esta clase puedes declarar varias 
    configuraciones de acuerdo con las necesidades del software.
    """

    def create_pizza(self, pizza_builder: PizzaBuilder) -> Pizza:
        pizza_builder.set_sauce()
        pizza_builder.set_ingredients()
        return pizza_builder.build()
    

if __name__ == '__main__':
    director = PizzaDirector()
    
    margherita_builder = MargheritaPizzaBuilder()
    new_york_builder = NewYorkPizzaBuilder()

    margherita_pizza = director.create_pizza(margherita_builder)
    new_york_pizza = director.create_pizza(new_york_builder)

    margherita_pizza.show_sauce()  
    margherita_pizza.show_ingredients()

    new_york_pizza.show_sauce()  
    new_york_pizza.show_ingredients()  
    