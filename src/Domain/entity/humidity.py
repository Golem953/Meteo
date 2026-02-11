"""AHumidity entity module."""
from dataclasses import dataclass
from domain.interface.imesure import IMesure

@dataclass
class Humidity(IMesure):
    """class representing humidity measurements."""
    value: float
    unit: str
    
    def __init__(self, value: int, unit: str) -> None:
        """Initializes the instance."""
        self.value = value
        self.unit = unit

    def get_value(self) -> float:
        """Gets the value."""
        return self.value

    def get_unit(self) -> str:
        """Gets the unit."""
        return self.unit