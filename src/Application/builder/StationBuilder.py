from Domain.config.Configuration import Configuration
from Infrastructure.extractor.APIDataExtractor import APIDataExtractor
from src.Domain.entity.AStation import AStation
from Infrastructure.interface.ICityStationProvider import ICityStationProvider
# from src.Infrastructure.mappers.CityMapper import CityMapper
from Application.interface.IBuilder import IBuilder
from src.Infrastructure.mappers.StationMapper import StationMapper
# from src.Infrastructure.provider.CityStationConfigMemoryProvider import CityStationConfigMemoryProvider
# from src.Infrastructure.http.APIClient import APIClient
from src.Infrastructure.mappers.RecordMapper import RecordMapper
# from src.Infrastructure.structures.LinkedList import LinkedList
# from src.Domain.entity.ANodeLinkedList import ANodeLinkedList


class StationBuilder(IBuilder):

    name: str
    _city_station_provider: ICityStationProvider
    station_mapper: StationMapper = StationMapper()
    record_mapper: RecordMapper = RecordMapper()
    

    def __init__(self, config: Configuration) -> None:
        self.api_data_extractor = APIDataExtractor(config)

    def set_name_station(self, name_station: str) -> None:
        self.name = name_station
        return self

    def set_city_station_provider(
        self, city_station_provider: ICityStationProvider
    ) -> None:
        self._city_station_provider = city_station_provider
        return self

    def build(self) -> AStation:
            
        file_name = self._city_station_provider.get_file_for_station(self.name)

        data_extracted = self.api_data_extractor.extract(file_name=file_name, limit=20)

        list_of_records = self.record_mapper.to_object(data=data_extracted)

        station = self.station_mapper.to_object(
            name=self.name, file_name=file_name, list_of_records=list_of_records
        )
        return station
