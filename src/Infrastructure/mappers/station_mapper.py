"""StationMapper infrastructure module."""
from domain.entity.station import Station
from domain.entity.record import Record
from infrastructure.interface.imappers import IMappers

class StationMapper(IMappers):
    """
    Mapper to convert JSON data of weather stations to Station objects.
    """

    def __init__(self):
        """Initializes the instance."""
        pass

    def to_object(self, name: str, file_name: str, list_of_records: list[Record]) -> Station:
        """Performs to object."""
        a_station = Station(name=name, file_name=file_name, list_of_records=list_of_records)
        return a_station