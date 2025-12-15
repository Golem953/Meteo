from src.Domain.entity.ACity import ACity
from src.Domain.entity.AStation import AStation
from src.Infrastructure.interface.IMappers import IMappers


class CityMapper(IMappers):
    """
    Mapper pour convertir les données de la ville
    depuis le format JSON vers un objet de domaine.
    """

    def __init__(self):
        pass

    def to_object(self, name: str, list_of_stations: list[AStation]) -> ACity:

        a_city = ACity(name=name, list_of_stations=list_of_stations)

        return a_city
