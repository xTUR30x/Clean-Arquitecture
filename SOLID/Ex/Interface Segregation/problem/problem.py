from abc import ABC, abstractmethod

class Worker(ABC):

    @abstractmethod
    def work(self) -> None:
        pass

    @abstractmethod
    def eat(self) -> None:
        pass

    @abstractmethod
    def sleep(self) -> None:
        pass

class Employee(Worker):

    def work(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def sleep(self) -> None:
        pass

class Robot(Worker):

    def work(self) -> None:
        pass

    def eat(self) -> None:
        raise Exception("Robots don't eat")

    def sleep(self) -> None:
        raise Exception("Robots don't sleep")

if __name__ == '__main__':
    robot = Robot()
    employee = Employee()

    lista = [robot, employee]

    for element in lista:
        element.eat()