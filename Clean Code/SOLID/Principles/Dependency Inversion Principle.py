#Dependency Inversion Principle

#Problem

class AccWeatherApi:

    def get_temperatureCelcius() -> int:
        pass


class BbcWeatherApi:

    def get_temperatureFahrenheit() -> float:
        pass



class WeatherAggregator:

    def __init__(self) -> None:

        self.acc_weather_api = AccWeatherApi()
        self.bbv_weather_api = BbcWeatherApi()


    def get_temperature(self) -> float: 
        return _to_celcius(0)


    def _to_celcius(self, temperature_fahrenheit: float):
        return (temperature_fahrenheit - 32 ) / 1.8;


#Solution

from abc import ABC, abstractmethod

class WeatherSource(ABC):

    @abstractmethod
    def get_temperature_celcius(self) -> float:
        pass


class AccWeatherApi(WeatherSource):

    def get_temperature_celcius(self):
        pass


class BbcWeatherApi(WeatherSource):

    def get_temperature_celcius(self) -> float:
        temp_fahrenheit = _get_temperature_fahrenheit()
        return _to_celcius(temp_fahrenheit)

    def _get_temperature_fahrenheit(self) -> float:
        pass

    def _to_celcius(self) -> float:
        pass

class WeatherAggregator:
    
    def __init__(self, weather_source):
        self.weather_source = weather_source

    def get_temperature(self) -> float:
        # Obtiene la temperatura promedio de todas las apis en Celcius
        pass