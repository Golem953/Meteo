"""CityMapper infrastructure module."""
from domain.entity.city import City
from domain.entity.station import Station
from infrastructure.interface.imappers import IMappers

class CityMapper(IMappers):
    """
    Mapper to convert city data from JSON format to a City object.
    """

    def __init__(self):
        """Initializes the instance."""
        pass

    def to_object(self, name: str, list_of_stations: list[Station]) -> City:
        """Performs to object."""
        a_city = City(name=name, list_of_stations=list_of_stations)
        return a_city