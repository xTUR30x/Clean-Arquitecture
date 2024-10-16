# State Pattern

from __future__ import annotations
from abc import ABC, abstractmethod

class VendingMachineState(ABC):

    @abstractmethod
    def insert_coin(self) -> None:
        pass

    @abstractmethod
    def select_product(self) -> None:
        pass

    @abstractmethod
    def dispense_product(self) -> None:
        pass
    

class NoCoinState(VendingMachineState):

    def __init__(self, machine: VendingMachine) -> None:
        self.machine = machine

    def insert_coin(self) -> None:
        print("Moneda insertada.")
        self.machine.set_has_coin_state()

    def select_product(self):
        print("Primero inserte una moneda.")

    def dispense_product(self):
        print("Primero inserte una moneda.")


class HasCoinState(VendingMachineState):

    def __init__(self, machine: VendingMachine):
        self.machine = machine

    def insert_coin(self):
        print("Ya hay una moneda insertada.")

    def select_product(self):
        print("Producto seleccionado.")
        self.machine.set_dispensing_state()

    def dispense_product(self):
        print("Primero seleccione un producto.")


class DispensingState(VendingMachineState):

    def __init__(self, machine: VendingMachine):
        self.machine = machine

    def insert_coin(self):
        print("Por favor, espere mientras se dispensa su producto.")

    def select_product(self):
        print("Por favor, espere mientras se dispensa su producto.")

    def dispense_product(self):
        print("Dispensando producto...")
        self.machine.set_no_coin_state()


class VendingMachine:
    """Contexto que mantiene una referencia al estado actual."""

    def __init__(self):
        self.state = NoCoinState(self)

    def set_state(self, state: VendingMachineState):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin()

    def select_product(self):
        self.state.select_product()

    def dispense_product(self):
        self.state.dispense_product()

    #States Changes

    def set_no_coin_state(self):
        self.state = NoCoinState(self)

    def set_dispensing_state(self):
        self.state = DispensingState(self)

    def set_has_coin_state(self):
        self.state = HasCoinState(self)


if __name__ == "__main__":
    vending_machine = VendingMachine()

    # Intentar seleccionar un producto sin insertar moneda
    vending_machine.select_product()

    # Insertar moneda
    vending_machine.insert_coin()

    # Seleccionar producto
    vending_machine.select_product()

    # Dispensar producto
    vending_machine.dispense_product()

    # Intentar dispensar nuevamente sin seleccionar otro producto
    vending_machine.dispense_product()