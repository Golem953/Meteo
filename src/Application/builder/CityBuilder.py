from src.Infrastructure.mappers.CityMapper import CityMapper
from src.Application.builder.IBuilder import IBuilder
from src.Infrastructure.mappers.StationMapper import StationMapper
from src.Infrastructure.mappers.RecordMapper import RecordMapper
from src.Infrastructure.http.APIClient import APIClient
from src.Domain.entity.ACity import ACity

class CityBuilder(IBuilder):
    def __init__(self, names: list[str], list_of_stations: list):
        self.names = names
        self.list_of_stations = list_of_stations
        self.city_mapper = CityMapper()
        self.station_mapper = StationMapper()
        self.record_mapper = RecordMapper()
        self.api_data_extractor = APIClient()

    def build(self) -> dict[str, ACity]:
        cities = {}
        
        for name in self.names:

            
            for stations in self.list_of_stations:
                
                data_extracted = self.api_data_extractor.extract(limit=20)

                list_of_records = self.record_mapper.to_object(data=data_extracted) 
             
                stations =  self.station_mapper.to_object(name=name, list_of_records=list_of_records)


            city = self.city_mapper.to_object(name=name, list_of_stations=stations)
            cities[name] = city

        return cities
            


        


     