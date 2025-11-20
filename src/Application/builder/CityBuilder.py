from Domain.ports.ICityStationProvider import ICityStationProvider
from src.Infrastructure.mappers.CityMapper import CityMapper
from Domain.ports.IBuilder import IBuilder
from src.Infrastructure.mappers.StationMapper import StationMapper
from src.Infrastructure.mappers.RecordMapper import RecordMapper
from src.Infrastructure.http.APIClient import APIClient
from src.Domain.entity.ACity import ACity

class CityBuilder(IBuilder):
    def __init__(self, names: list[str], city_station_provider: ICityStationProvider):
        self.names = names
        self.city_mapper = CityMapper()
        self.station_mapper = StationMapper()
        self.record_mapper = RecordMapper()
        self.api_data_extractor = APIClient()
        self._city_station_provider = city_station_provider

    def build(self) -> dict[str, ACity]:
        cities: dict[str, ACity] = {}
        
        for name in self.names:
            station_keys = self._city_station_provider.get_stations_for_city(name)
            stations = []
            
            for station_key in station_keys:

                file_name = self._city_station_provider.get_file_for_station(station_key)
                if not file_name:
                    continue  # ou log/raise
                
                data_extracted = self.api_data_extractor.extract(file_name=file_name, limit=20)

                list_of_records = self.record_mapper.to_object(data=data_extracted) 
             
                stations.append(self.station_mapper.to_object(name=station_key, list_of_records=list_of_records))


            city = self.city_mapper.to_object(name=name, list_of_stations=stations)
            cities[name] = city

        return cities
            


        


     