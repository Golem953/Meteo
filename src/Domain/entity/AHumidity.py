"""AHumidity entity module."""
from domain.interface.IMesure import IMesure

class AHumidity(IMesure):
    """Abstract class representing humidity measurements."""

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