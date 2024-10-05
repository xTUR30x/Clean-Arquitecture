#Command Pattern

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class SaveCommand(Command):
    def execute(self):
        print("Archivo guardado.")

class LoadCommand(Command):
    def execute(self):
        print("Archivo cargado.")

class UndoCommand(Command):
    def execute(self):
        print("Última acción deshecha.")

class Button:
    def __init__(self, label: str, command: Command):
        self.label = label
        self.command = command

    def press(self):
        print(f"Botón '{self.label}' presionado.")
        self.command.execute()


if __name__ == '__main__':
    # Uso del patrón Command con botones
    save_button = Button("Guardar", SaveCommand())
    load_button = Button("Cargar", LoadCommand())
    undo_button = Button("Deshacer", UndoCommand())

    # Simular presionar los botones
    save_button.press()
    load_button.press()
    undo_button.press()