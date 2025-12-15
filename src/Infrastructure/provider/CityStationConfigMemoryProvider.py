from typing import List, Optional

from Infrastructure.interface.ICityStationProvider import ICityStationProvider


class CityStationConfigMemoryProvider(ICityStationProvider):

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._mapping = {
                "toulouse": {
                    "compans cafarelli": "42-station-meteo-toulouse-parc-compans-cafarelli",
                    "universite paul sabatier": "37-station-meteo-toulouse-universite-paul-sabatier",
                }
            } 
        return cls._instance

    def get_stations_for_city(self, city: str) -> List[str]:

        city_key = city.lower()
        stations = self._mapping.get(city_key, {})

        return list(stations.keys())

    def get_file_for_station(self, station_key: str) -> Optional[str]:
        key = station_key.lower()
        for stations in self._mapping.values():
            if key in stations:
                return stations[key]
        return None
