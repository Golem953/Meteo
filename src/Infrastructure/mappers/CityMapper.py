"""CityMapper infrastructure module."""
from domain.entity.ACity import ACity
from domain.entity.AStation import AStation
from infrastructure.interface.IMappers import IMappers

class CityMapper(IMappers):
    """
    Mapper pour convertir les données de la ville
    depuis le format JSON vers un objet de domaine.
    """

    def __init__(self):
        """Initializes the instance."""
        pass

    def to_object(self, name: str, list_of_stations: list[AStation]) -> ACity:
        """Performs to object."""
        a_city = ACity(name=name, list_of_stations=list_of_stations)
        return a_city