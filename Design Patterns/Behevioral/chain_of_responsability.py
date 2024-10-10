# Chain of Responsability Pattern

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    """
    El comportamiento de encadenamiento predeterminado puede ser implementado
    dentro de una clase base.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None
    
class CustomerServiceHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Simple Complaint":
            return f"Customer Service: Handling '{request}'"
        else:
            return super().handle(request)


class SupervisorHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Moderate Complaint":
            return f"Supervisor: Handling '{request}'"
        else:
            return super().handle(request)


class ManagerHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Serious Complaint":
            return f"Manager: Handling '{request}'"
        else:
            return super().handle(request)
        
def client_code(handler: Handler) -> None:
    """
    El código del cliente suele estar diseñado para trabajar con un solo manejador.
    En la mayoría de los casos, ni siquiera es consciente de que el manejador es parte de una cadena.
    """

    for complaint in ["Simple Complaint", "Moderate Complaint", "Serious Complaint", "Unknown Issue"]:
        print(f"\nClient: What about '{complaint}'?")
        result = handler.handle(complaint)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  '{complaint}' was left unattended.", end="")


if __name__ == "__main__":
    customer_service = CustomerServiceHandler()
    supervisor = SupervisorHandler()
    manager = ManagerHandler()

    # Configuramos la cadena de responsabilidad
    customer_service.set_next(supervisor).set_next(manager)

    print("Chain: Customer Service > Supervisor > Manager")
    
    # Ejecutamos el código del cliente con la cadena configurada
    client_code(customer_service)