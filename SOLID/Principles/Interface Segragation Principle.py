#Interface Segragation Principle

#Problem

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fly(self) -> None:
        pass


    @abstractmethod
    def drive(self) -> None:
        pass


class Car(Vehicle):

    def fly(self) -> None:

        raise Exception("Cars don't fly")
    

    def drive(self) -> None:
        pass


class Plane(Vehicle):

    def fly(self) -> None:
        pass
    

    def drive(self) -> None:

        raise Exception("Planes don't drive")



if __name__ == '__main__':
    car: Vehicle = Car()
    plane: Vehicle = Plane()

    car.drive()
    plane.fly()


#Solution

class Drivable(ABC):

    @abstractmethod
    def drive(self) -> None:
        pass

class Flyable(ABC):

    @abstractmethod
    def fly(self) -> None:
        pass


class Car(Drivable):

    def drive(self) -> None:
        pass

class Plane(Flyable): 

    def fly(self) -> None:
        pass

if __name__ == '__main__':
    car: Drivable = Car()
    plane: Flyable = Plane()

    car.drive()
    plane.fly()




