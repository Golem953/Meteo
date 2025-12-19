"""City builder module."""

from application.builder.StationBuilder import StationBuilder
from domain.entity.ANodeQueueList import ANodeQueueList
from infrastructure.interface.ICityStationProvider import ICityStationProvider
from infrastructure.structures.QueueList import QueueList
from infrastructure.mappers.CityMapper import CityMapper
from application.interface.IBuilder import IBuilder
from domain.entity.ACity import ACity
from domain.config.Configuration import Configuration


class CityBuilder(IBuilder):
    """Builder class for creating City objects."""

    names_city: list[str]
    stations_choose: list[str]
    city_mapper: CityMapper = CityMapper()
    _city_station_provider: ICityStationProvider

    def __init__(self) -> None:
        """Initializes the CityBuilder instance."""
        pass

    def set_names_city(self, names_city: list[str]) -> None:
        """Sets the list of city names."""
        self.names_city = names_city
        return self

    def set_stations_choose(self, stations_choose: list[str]) -> None:
        """Sets the list of stations to choose."""
        self.stations_choose = stations_choose
        return self

    def set_city_station_provider(
        self, city_station_provider: ICityStationProvider
    ) -> None:
        """Sets the city station provider."""
        self._city_station_provider = city_station_provider
        return self

    def build(self) -> dict[str, ACity]:
        """Builds and returns a dictionary of cities."""
        if self.names_city is None:
            raise ValueError("Names of cities not set")
        if self.stations_choose is None:
            raise ValueError("Stations to choose not set")
        if self._city_station_provider is None:
            raise ValueError("City station provider not set")
        cities: dict[str, ACity] = {}
        config = Configuration()
        for name_city in self.names_city:
            station_keys = self._city_station_provider.get_stations_for_city(name_city)
            stations = []
            first_station = True
            for station_key in station_keys:
                if station_key in self.stations_choose:
                    if first_station:
                        linked_list_station = QueueList(ANodeQueueList(station_key))
                        first_station = False
                    else:
                        linked_list_station.add_node(ANodeQueueList(station_key))
        actual_node = linked_list_station.first_node
        while actual_node is not None:
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
