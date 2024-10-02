class ShapeCalculator:

    def calculate_total_areas(self, shapes:list) -> float:
        total_area = 0

        for shape in shapes:
            total_area = 0 
            total_area += shape.get_area()

        return total_area