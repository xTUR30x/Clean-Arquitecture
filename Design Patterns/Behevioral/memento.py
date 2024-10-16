# Memento Pattern

class Memento:
    def __init__(self, text: str) -> None:
        self.text = text

    

class Editor:
    def __init__(self) -> None:
        self.text = ""

    def write(self, text: str) -> None:
        self.text += text

    def save(self) -> Memento:
        return Memento(self.text)
    
    def restore(self, memento: Memento) -> None:
        self.text = memento.text


class Caretaker:
    def __init__(self) -> None:
        self.mementos = []

    def save_memento(self, editor: Editor):
        save = editor.save()
        self.mementos.append(save)

    def restore_memento(self, editor: Editor):
        if self.mementos:
            last_memento = self.mementos.pop()
            editor.restore(last_memento)


if __name__ == "__main__":
    # Crear el editor y el cuidador
    editor = Editor()
    caretaker = Caretaker()

    # Escribir texto y guardar estados
    editor.write("Hola, ")
    caretaker.save_memento(editor)

    editor.write("mundo!")
    caretaker.save_memento(editor)

    print("Texto actual:", editor.text)

    # Deshacer la última acción
    caretaker.restore_memento(editor)
    print("Después de deshacer:", editor.text)