#Flyweight Pattern

class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int):
        print(f"Dibujando un {self.color} {self.name} en ({x}, {y}) con textura {self.texture}.")

class Tree:
    def __init__(self, tree_type: TreeType, x: int, y: int) -> None:
        self.tree_type = tree_type
        self.x = x
        self.y = y

    def draw(self):
        self.tree_type.draw(self.x, self.y)

class TreeFactory:
    def __init__(self) -> None:
        self.tree_types = {}

    def get_tree_type(self, name: str, color: str, texture:str):

        key = (name, color, texture)

        if key not in self.tree_types:
            self.tree_types[key] = TreeType(name, color, texture)

        return self.tree_types[key]
    
class Forest:
    def __init__(self) -> None:
        self.trees = []
        self.tree_factory = TreeFactory()

    def add_tree(self, name: str, color:str, texture: str, x: int, y:int):
        tree_type = self.tree_factory.get_tree_type(name, color, texture)
        tree = Tree(tree_type, x, y)
        self.trees.append(tree)

    def draw_forest(self):
        for tree in self.trees:
            tree.draw()

if __name__ == "__main__":
    forest = Forest()

    # Crear un bosque con diferentes tipos de árboles
    forest.add_tree("Pino", "Verde", "Agujas", 10, 20)
    forest.add_tree("Roble", "Marrón", "Hoja", 15, 25)
    forest.add_tree("Pino", "Verde", "Agujas", 30, 40)  # Reutiliza el Pino

    # Dibujar todos los árboles en el bosque
    forest.draw_forest()