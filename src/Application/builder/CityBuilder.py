from Application.builder.StationBuilder import StationBuilder
from Domain.ports.ICityStationProvider import ICityStationProvider
from src.Infrastructure.mappers.CityMapper import CityMapper
from Domain.ports.IBuilder import IBuilder
from src.Infrastructure.mappers.StationMapper import StationMapper
from src.Infrastructure.mappers.RecordMapper import RecordMapper
from src.Infrastructure.http.APIClient import APIClient
from src.Domain.entity.ACity import ACity
from src.Infrastructure.structures.LinkedList import LinkedList
from src.Domain.entity.ANodeLinkedList import ANodeLinkedList


class CityBuilder(IBuilder):
    def __init__(
        self,
        names_city: list[str],
        stations_choose: list[str],
        city_station_provider: ICityStationProvider,
    ):
        self.names_city = names_city
        self.stations_choose = stations_choose
        self.city_mapper = CityMapper()
        self.station_mapper = StationMapper()
        self.record_mapper = RecordMapper()
        self.api_data_extractor = APIClient()
        self._city_station_provider = city_station_provider

    def build(self) -> dict[str, ACity]:
        cities: dict[str, ACity] = {}
        # print("Building cities...")
        for name_city in self.names_city:

            station_keys = self._city_station_provider.get_stations_for_city(name_city)

            stations = []

            first_station = True
            for station_key in station_keys:

                if station_key in self.stations_choose:

                    if first_station:

                        linked_list_station = LinkedList(ANodeLinkedList(station_key))
                        first_station = False
                    else:

                        linked_list_station.add_node(ANodeLinkedList(station_key))

        actual_node = linked_list_station.first_node

        while actual_node != None:

            stations.append(
                StationBuilder(
                    name_station=actual_node.get_value(),
                    city_station_provider=self._city_station_provider,
                ).build()
            )

            actual_node = actual_node.get_next()

        city = self.city_mapper.to_object(name=name_city, list_of_stations=stations)
        cities[name_city] = city

        return cities
