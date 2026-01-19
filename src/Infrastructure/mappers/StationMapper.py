"""StationMapper infrastructure module."""
from domain.entity.AStation import AStation
from domain.entity.ARecord import ARecord
from infrastructure.interface.IMappers import IMappers

class StationMapper(IMappers):
    """
    Mapper to convert JSON data of weather stations to AStation objects.
    """

    def __init__(self):
        """Initializes the instance."""
        pass

    def to_object(self, name: str, file_name: str, list_of_records: list[ARecord]) -> AStation:
        """Performs to object."""
        a_station = AStation(name=name, file_name=file_name, list_of_records=list_of_records)
        return a_station