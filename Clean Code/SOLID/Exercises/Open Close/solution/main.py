from shape_calculator import ShapeCalculator
from circle import Circle
from rectangle import Rectangle

if __name__ == '__main__':
    shape_calculator = ShapeCalculator()
    circle = Circle(2)
    rectangle = Rectangle(2, 4)

    shapes = [circle, rectangle]

    print(shape_calculator.calculate_total_areas(shapes))
    