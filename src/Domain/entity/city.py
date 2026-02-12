"""City entity module."""

from domain.entity.station import Station


class City:
    """class representing a City entity."""

    def __init__(self, name: str, list_of_stations: list[Station]):
        """Initializes the instance."""
        self.name = name
        self.stations = list_of_stations
