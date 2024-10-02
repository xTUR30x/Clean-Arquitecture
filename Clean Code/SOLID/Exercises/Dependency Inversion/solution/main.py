from car import Car
from electric_engine import ElectricEngine
from gasoline_engine import GasolineEngine

if __name__ == '__main__':
    electric_engine = ElectricEngine()
    gasoline_engine = GasolineEngine()

    electric_car = Car(electric_engine)
    gasoline_car = Car(gasoline_engine)

    lista = [electric_car, gasoline_car]

    for i in lista:
        i.start()