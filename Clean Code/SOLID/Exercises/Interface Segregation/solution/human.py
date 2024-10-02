from abc import ABC, abstractmethod

class Human(ABC):

    @abstractmethod
    def eat(self) -> None:
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        pass