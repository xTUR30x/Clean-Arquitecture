from polygon import Polygon

class Square(Polygon):

    def __init__(self, side:int):
        self._side = side

    def set_side(self, side:int) -> None:
        self._side = side

    def get_area(self):
        return self._side ** 2
    