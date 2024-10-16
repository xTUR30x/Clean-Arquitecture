# Template Method

from abc import ABC, abstractmethod

class Beverage(ABC):

    def prepare(self) -> None:
        self.boil_water()
        self.add_ingredients()
        self.stir()

    @abstractmethod
    def add_ingredients(self) -> None:
        pass

    def boil_water(self) -> None:
        print("Boling water")

    def stir(self) -> None:
        print("Stirring Bevarage")


class Tea(Beverage):
    
    def add_ingredients(self) -> None:
        print("Adding tea leaves...")


class Coffee(Beverage):
    
    def add_ingredients(self) -> None:
        print("Adding coffee grounds...")


if __name__ == '__main__':
    print("Preparing Tea:")
    tea = Tea()
    tea.prepare()
    
    print("----------------------")

    print("Preparing Coffee:")
    coffee = Coffee()
    coffee.prepare()
    