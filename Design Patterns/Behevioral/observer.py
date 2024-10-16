#Observer Pattern

from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, temperature: float, humidity: float) -> None:
        pass

class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class WeatherStation(Subject):
    def __init__(self) -> None:
        self._observers = []
        self._temperature = 0.0
        self._humidity = 0.0

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

    def set_measurements(self, temperature: float, humidity: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.notify()


class MobileApp(Observer):
    def update(self, temperature: float, humidity: float) -> None:
        print(f"Aplicación Móvil: Temperatura actual es {temperature}°C y humedad es {humidity}%.")


class WeatherDisplay(Observer):
    def update(self, temperature: float, humidity: float) -> None:
        print(f"Estación Meteorológica: Temperatura actual es {temperature}°C y humedad es {humidity}%.")



if __name__ == "__main__":
    # Crear la estación meteorológica y las aplicaciones que la observan
    weather_station = WeatherStation()
    
    mobile_app = MobileApp()
    weather_display = WeatherDisplay()

    # Adjuntar las aplicaciones a la estación meteorológica
    weather_station.attach(mobile_app)
    weather_station.attach(weather_display)

    # Simular cambios en las mediciones del clima
    weather_station.set_measurements(25.0, 60)
    weather_station.set_measurements(30.0, 55)