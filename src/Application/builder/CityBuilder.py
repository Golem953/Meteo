from Application.builder.StationBuilder import StationBuilder
from Domain.entity.ANodeQueueList import ANodeQueueList
from Infrastructure.interface.ICityStationProvider import ICityStationProvider
from Infrastructure.structures.QueueList import QueueList
from src.Infrastructure.mappers.CityMapper import CityMapper
from Application.interface.IBuilder import IBuilder
from src.Domain.entity.ACity import ACity
from src.Infrastructure.structures.LinkedList import LinkedList
from src.Domain.entity.ANodeLinkedList import ANodeLinkedList
from Domain.config.Configuration import Configuration

class CityBuilder(IBuilder):

    names_city: list[str]
    stations_choose: list[str]
    city_mapper: CityMapper = CityMapper()
    _city_station_provider: ICityStationProvider

    def __init__(self) -> None:
        pass

    def set_names_city(self, names_city: list[str]) -> None:
        self.names_city = names_city
        return self

    def set_stations_choose(self, stations_choose: list[str]) -> None:
        self.stations_choose = stations_choose
        return self

    def set_city_station_provider(
        self, city_station_provider: ICityStationProvider
    ) -> None:
        self._city_station_provider = city_station_provider
        return self

    def build(self) -> dict[str, ACity]:

        if self.names_city is None:
            raise ValueError("Names of cities not set")
        if self.stations_choose is None:
            raise ValueError("Stations to choose not set")
        if self._city_station_provider is None:
            raise ValueError("City station provider not set")

        cities: dict[str, ACity] = {}

        config = Configuration()

        
        # print("Building cities...")
        for name_city in self.names_city:

            station_keys = self._city_station_provider.get_stations_for_city(name_city)

            stations = []

            first_station = True
            for station_key in station_keys:

                if station_key in self.stations_choose:

                    if first_station:

                        linked_list_station = QueueList(ANodeQueueList(station_key))
                        # linked_list_station = LinkedList(ANodeLinkedList(station_key))

                        first_station = False
                    else:

                        linked_list_station.add_node(ANodeQueueList(station_key))
                        # linked_list_station.add_node(ANodeLinkedList(station_key))
        actual_node = linked_list_station.first_node

        while actual_node != None:

            station_builder = (
                StationBuilder(config)
                .set_name_station(actual_node.get_value())
                .set_city_station_provider(self._city_station_provider)
                .build()
            )

            stations.append(station_builder)

            actual_node = actual_node.get_next()

        city = self.city_mapper.to_object(name=name_city, list_of_stations=stations)
        cities[name_city] = city

        return cities
