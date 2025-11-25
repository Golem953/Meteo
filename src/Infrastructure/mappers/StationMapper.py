from src.Domain.entity.AStation import AStation
from src.Domain.entity.ARecord import ARecord
from src.Domain.ports.IMappers import IMappers


class StationMapper(IMappers):
    """
    Mapper pour convertir les données JSON des stations météorologiques 
    vers des objets de domaine AStation.
    """

    def __init__(self):
        pass

    def to_object(self, name: str, list_of_records: list[ARecord]) -> AStation:

        a_station = AStation(name=name, list_of_records=list_of_records)

        return a_station
