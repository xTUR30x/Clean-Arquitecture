from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def get_area(self) -> float:
        pass