from polygon import Polygon

class Rectangle(Polygon):

    def __init__(self, height:int, width:int) -> None:
        self._height = height
        self._width = width

    def set_height(self, height:int) -> None:
        self._height = height

    def set_width(self, width:int) -> None:
        self._width = width

    def get_area(self):
        return self._width * self._height