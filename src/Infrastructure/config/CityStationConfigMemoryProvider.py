from typing import List, Optional

from Domain.ports.ICityStationProvider import ICityStationProvider


class CityStationConfigMemoryProvider(ICityStationProvider):

    def __init__(self) -> None:
        self._mapping: dict[str, str] = {
            "toulouse": {
                "compans cafarelli": "42-station-meteo-toulouse-parc-compans-cafarelli",
                "université paul sabatier": "37-station-meteo-toulouse-universite-paul-sabatier",
            }
        }

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
