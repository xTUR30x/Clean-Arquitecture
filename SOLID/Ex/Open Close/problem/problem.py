class ShapeCalculator:

    def calculate_total_areas(self, shapes:list) -> float:
        total_area = 0

        for shape in shape:
            if isinstance(shape, Circle):
                pass
            elif isinstance(shape, Rectangle):
                pass


class Shape:
    pass


class Circle(Shape):

    def __init__(self, radius:float) -> None:
        self.radius = radius

    def get_area(self):
        return self.radius


class Rectangle(Shape):

    def __init__(self, width:flaot, length:float) -> None:
        self.length = length
        self.width = width
    
    def get_length(self) -> float:
        return self.length

    def get_width(self) -> float:
        return self.width
