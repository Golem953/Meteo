"""ACity entity module."""

from domain.entity.AStation import AStation


class ACity:
    """Abstract class representing a City entity."""

    def __init__(self, name: str, list_of_stations: list[AStation]):
        """Initializes the instance."""
        self.name = name
        self.stations = list_of_stations
