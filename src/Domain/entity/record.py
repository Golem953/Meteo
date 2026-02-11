"""Record domain module."""

from domain.entity.temperature import Temperature
from domain.entity.humidity import Humidity
from domain.entity.pressure import Pressure


class Record:
    """class representing weather records."""

    def __init__(
        self,
        id: int,
        paris_date: str,
        temperature: Temperature,
        humidity: Humidity,
        pressure: Pressure,
    ) -> None:
        """Initializes the instance."""
        self.id = id
        self.paris_date = paris_date
        self.temperature: Temperature = temperature
        self.humidity: Humidity = humidity
        self.pressure: Pressure = pressure

    def __repr__(self) -> str:
        """Returns a string representation of the instance."""
        return f"Record(id={self.id}, paris_date={self.paris_date}, temperature={self.temperature.get_value()} {self.temperature.get_unit()}, humidity={self.humidity.get_value()} {self.humidity.get_unit()}, pressure={self.pressure.get_value()} {self.pressure.get_unit()})"
