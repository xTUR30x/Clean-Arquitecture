#Liskov Substitution Principle

#Problem

class Bird:

    def fly(self):
        pass

    def eat(self):
        pass

class Crow(Bird):

    def fly(self):
        pass

    def eat(self):
        pass

class Ostrich(Bird):

    def fly(self):
        raise Exception("Ostrich can't fly")

    def eat(self):
        pass

if __name__ == '__main__':

    crow = Crow()
    ostrich = Ostrich()
    birds = [crow, ostrich]

    for bird in birds:
        bird.fly()
    
#Solution

from ABC import ABC

class Bird(ABC):

    @abstractmethod
    def eat(self):
        pass

class FlyingBird(Bird):
    
    @abstractmethod
    def fly(self):
        pass

class Crow(FlyingBird):

    def fly(self):
        pass

    def eat(self):
        pass

class Ostrich(Bird):

    def eat(self):
        pass


if __name__ == '__main__':
    crow = Crow()
    ostrich = Ostrich()

    birds: Bird = [crow, ostrich]
    flying_birds: FlyingBird = [crow]

    for bird in birds:
        bird.eat()

    for bird in flying_birds:
        bird.fly()
