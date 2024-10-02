#Singleton Pattern

from typing import Any


class SingletonMeta(type):
    """
    Metaclase para implementar el patrón Singleton.
    Asegura que solo exista una instancia de la clase.
    """

    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance

        return cls._instances[cls]
    
class SingletonTest(metaclass=SingletonMeta):
    
    def __init__(self) -> None:
        self._value = None

    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, new_value:str) -> None:
        self._value = new_value


if __name__ == '__main__':
    singleton = SingletonTest()

    singleton.value = "Hola"

    print(singleton.value)
