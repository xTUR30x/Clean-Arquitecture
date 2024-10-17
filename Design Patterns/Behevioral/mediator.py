# Mediator Pattern

from __future__ import annotations
from abc import ABC, abstractmethod

class Mediator(ABC):

    @abstractmethod
    def send(self, message: str, sender_user: User) -> None:
        pass


class ChatMediator(Mediator):

    def __init__(self) -> None:
        self.users = []

    def register_user(self, user: User) -> None:
        self.users.append(user)

    def send(self, message: str, sender_user: User) -> None:
        
        for user in self.users:
            if user != sender_user:
                user.receive(message)


class User(ABC):

    def __init__(self, mediator: Mediator, name: str) -> None:
        self.mediator = mediator

    @abstractmethod
    def send(self, message: str) -> None:
        pass

    @abstractmethod
    def receive(self, message: str) -> None:
        pass


class ConcreteUser(User):
    def __init__(self, mediator: Mediator, name: str) -> None:
        super().__init__(mediator, name)
        self.name = name

    def send(self, message: str):
        print(f"{self.name} envía: {message}")
        self.mediator.send(message, self)

    def receive(self, message: str):
        print(f"{self.name} recibió: {message}")


if __name__ == "__main__":
    # Crear el mediador
    mediator = ChatMediator()

    # Crear usuarios
    user1 = ConcreteUser(mediator, "Usuario 1")
    user2 = ConcreteUser(mediator, "Usuario 2")

    # Registrar usuarios en el mediador
    mediator.register_user(user1)
    mediator.register_user(user2)

    # Enviar mensajes
    user1.send("Hola, ¿cómo estás?")
    user2.send("¡Estoy bien! ¿Y tú?")
