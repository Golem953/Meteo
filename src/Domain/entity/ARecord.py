"""ARecord domain module."""

from domain.entity.ATemperature import ATemperature
from domain.entity.AHumidity import AHumidity
from domain.entity.APressure import APressure


class ARecord:
    """Abstract class representing weather records."""

    def __init__(
        self,
        id: int,
        paris_date: str,
        temperature: ATemperature,
        humidity: AHumidity,
        pressure: APressure,
    ) -> None:
        """Initializes the instance."""
        self.id = id
        self.paris_date = paris_date
        self.temperature: ATemperature = temperature
        self.humidity: AHumidity = humidity
        self.pressure: APressure = pressure

    def __repr__(self) -> str:
        """Returns a string representation of the instance."""
        return f"ARecord(id={self.id}, paris_date={self.paris_date}, temperature={self.temperature.get_value()} {self.temperature.get_unit()}, humidity={self.humidity.get_value()} {self.humidity.get_unit()}, pressure={self.pressure.get_value()} {self.pressure.get_unit()})"
