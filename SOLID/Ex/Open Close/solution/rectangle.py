from shape import Shape

class Rectangle(Shape):

    def __init__(self, width:float, length:float) -> None:
        self.length = length
        self.width = width
    
    def get_length(self) -> float:
        return self.length

    def get_width(self) -> float:
        return self.width

    def get_area(self) -> float:
        return self.width * self.length