from src.Domain.AStation import AStation

class ACity:
    def __init__(self, id: int, nom: str, list_of_stations: list[AStation]):
        self.id = id
        self.nom = nom
        self.list_of_stations = list_of_stations
