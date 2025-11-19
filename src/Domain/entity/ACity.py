from src.Domain.entity.AStation import AStation

class ACity:
    def __init__(self, nom: str, list_of_stations: list[AStation]):
        self.nom = nom
        self.list_of_stations = list_of_stations