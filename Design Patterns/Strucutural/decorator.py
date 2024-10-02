#Decorator Pattern

class Coffee:
    def costo(self):
        return 5
    
class Decorator:
    def __init__(self) -> None:
        self.coffee = Coffee()

    def costo(self):
        return self.coffee.costo()
    

class Milk(Decorator):
    def costo(self):
        return self.coffee.costo() + 1
    
class Sugar(Decorator):
    def costo(self):
        return self.coffee.costo() + 0.5
    

if __name__ == '__main__':
    coffee = Coffee()
    coffee_milk = Milk(coffee)
    coffee_sugar = Sugar(coffee)
