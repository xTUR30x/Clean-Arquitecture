from shape import Shape

class Circle(Shape):

    def __init__(self, radius:float) -> None:
        self.radius = radius

    def get_area(self) -> float:
        return self.radius

    def get_area(self) -> float:
        return self.radius * (3.14 ** 2.0)