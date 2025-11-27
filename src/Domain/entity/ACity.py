from src.Domain.entity.AStation import AStation


class ACity:
    def __init__(self, name: str, list_of_stations: list[AStation]):
        self.name = name
        self.stations = list_of_stations
