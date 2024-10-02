import copy
from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self, name: str) -> None:
        self.name = name
        self.axis = ['x', 'y']

    @abstractmethod
    def copy(self):
        """
        Crea una copia parcial del objeto en cuestion (no mantiene las referencias de sus atributos)
        """

        raise NotImplementedError("Este método debe ser implementado por las subclases.")
    
    @abstractmethod
    def deep_copy(self):
        """
        Crea una nueva copia del objeto en cuestion (no mantiene las referencias de sus atributos)
        """

        raise NotImplementedError("Este método debe ser implementado por las subclases.")
    

class Circulo(Figura):

    def __init__(self, name: str, radio: int) -> None:
        super().__init__(name)
        self.radio = radio

    def copy(self):
        return copy.copy(self)
    
    def deep_copy(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    c = Circulo("Circulo", 10)

    c1 = c.copy()
    c2 = c.deep_copy()

    c1.name = "Circulo1"
    c2.name = "Circulo2"

    c.axis.append('z')
    c2.axis.append('w')

    print(c.name, c1.name, c2.name)

    print(c.axis, c1.axis, c2.axis)