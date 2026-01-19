"""CityStationConfigMemoryProvider infrastructure module."""
from typing import List, Optional
from infrastructure.interface.ICityStationProvider import ICityStationProvider

class CityStationConfigMemoryProvider(ICityStationProvider):
    """Provider for city-station configuration(in memory) mappings."""

    _instance = None

    def __new__(cls):
        """Performs new."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._mapping = {'toulouse': {'compans cafarelli': '42-station-meteo-toulouse-parc-compans-cafarelli', 'universite paul sabatier': '37-station-meteo-toulouse-universite-paul-sabatier'}}
        return cls._instance

    def get_stations_for_city(self, city: str) -> List[str]:
        """Gets the stations for city."""
        city_key = city.lower()
        stations = self._mapping.get(city_key, {})
        return list(stations.keys())

    def get_file_for_station(self, station_key: str) -> Optional[str]:
        """Gets the file for station."""
        key = station_key.lower()
        for stations in self._mapping.values():
            if key in stations:
                return stations[key]
        return None