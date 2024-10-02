from abc import ABC, abstractmethod

class Polygon:

    @abstractmethod
    def get_area(self) -> int:
        pass
