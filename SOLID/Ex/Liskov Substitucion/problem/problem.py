
class Rectangle:

    def __init__(self):
        self._width
        self._height

    def set_width(width: int) -> None:
        self._width = width

    def set_height(height: int) -> None:
        self._height = height

    def calculateArea() -> int:
        return self.width * self.height;


class Square(Rectangle):
    
    def __init__(self):
        super().__init__()

    def set_width(width: int) -> None:
        self._width = width

    def set_height(height: int) -> None:
        self._height = height
        


if __name__ == '__main__':
    square: Rectangle = Square()
    Rectangle: Rectangle = Rectangle()

    print(square.calculateArea)
    print(square.calculateArea)