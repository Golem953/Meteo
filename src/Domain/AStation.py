from src.Domain.ARecord import ARecord


class AStation:
    def __init__(self, id: int, nom: str, list_of_stations: list[ARecord]):
        self.id = id
        self.nom = nom
        self.list_of_stations = list_of_stations
