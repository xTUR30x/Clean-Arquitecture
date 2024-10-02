from rectangle import Rectangle
from square import Square

if __name__ == '__main__':
    rectangle = Rectangle(5, 10)
    square = Square(5)

    polygons = [rectangle, square]

    for polygon in polygons:
        print(polygon.get_area())
    