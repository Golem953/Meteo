from src.Domain.Interfaces import IHumidity
from src.Domain.Interfaces import ITemperature
from src.Domain.Interfaces import IPressure

class WeatherMeasurement(IHumidity, ITemperature, IPressure):
    def __init__(self):
        pass
    def get_humidity_now(self) -> float:
        pass
    def get_temperature_now (self) -> float:
        pass
    def get_pressure_now(self) -> float:
        pass
