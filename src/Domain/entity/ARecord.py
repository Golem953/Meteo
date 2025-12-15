from src.Domain.entity.ATemperature import ATemperature
from src.Domain.entity.AHumidity import AHumidity
from src.Domain.entity.APressure import APressure

class ARecord:
    def __init__(self, id: int, paris_date: str, temperature: ATemperature, humidity: AHumidity, pressure: APressure) -> None:
        self.id = id
        self.paris_date = paris_date
        self.temperature:ATemperature = temperature
        self.humidity:AHumidity = humidity
        self.pressure:APressure = pressure

    def __repr__(self):
        return (f"ARecord(id={self.id}, paris_date={self.paris_date}, "
                f"temperature={self.temperature.get_value()} {self.temperature.get_unit()}, humidity={self.humidity.get_value()} {self.humidity.get_unit()}, "
                f"pressure={self.pressure.get_value()} {self.pressure.get_unit()})")
