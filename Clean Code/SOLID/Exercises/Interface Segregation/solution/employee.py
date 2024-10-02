from human import Human
from worker import Worker

class Employee(Human, Worker):

    def work(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def sleep(self) -> None:
        pass