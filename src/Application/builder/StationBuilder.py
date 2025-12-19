"""Station builder module."""

from domain.config.Configuration import Configuration
from infrastructure.extractor.APIDataExtractor import APIDataExtractor
from domain.entity.AStation import AStation
from infrastructure.interface.ICityStationProvider import ICityStationProvider
from application.interface.IBuilder import IBuilder
from infrastructure.mappers.StationMapper import StationMapper
from infrastructure.mappers.RecordMapper import RecordMapper


class StationBuilder(IBuilder):
    """Builder class for creating Station objects."""

    name: str
    _city_station_provider: ICityStationProvider
    station_mapper: StationMapper = StationMapper()
    record_mapper: RecordMapper = RecordMapper()

    def __init__(self, config: Configuration) -> None:
        """Initializes the instance."""
        self.api_data_extractor = APIDataExtractor(config)

    def set_name_station(self, name_station: str) -> None:
        """Sets the name station."""
        self.name = name_station
        return self

    def set_city_station_provider(
        self, city_station_provider: ICityStationProvider
    ) -> None:
        """Sets the city station provider."""
        self._city_station_provider = city_station_provider
        return self

    def build(self) -> AStation:
        """Builds the object."""
        file_name = self._city_station_provider.get_file_for_station(self.name)
        data_extracted = self.api_data_extractor.extract(file_name=file_name, limit=20)
        list_of_records = self.record_mapper.to_object(data=data_extracted)
        station = self.station_mapper.to_object(
            name=self.name, file_name=file_name, list_of_records=list_of_records
        )
        return station
