import unittest

# 1.Escribe una prueba para una nueva funcionalidad. Esta prueba debe fallar inicialmente porque la funcionalidad aún no está implementada.
# 2.Escribe el código mínimo necesario para hacer que la prueba pase.
# 3.Mejora el código, optimizándolo y asegurándote de que sigue pasando todas las pruebas.

#1
class TestCalculator(unittest.TestCase):
    def test_add(self):
        operation = add(2,3)
        self.assertEqual(operation, 5)

def add(a: int, b: int) -> int:
    pass


#2
def add(a: int, b: int) -> int:
    result = a + b
    return result

#3
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    unittest.main()