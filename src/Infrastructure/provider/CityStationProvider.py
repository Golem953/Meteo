import json
from typing import Dict, List, Optional
from Domain.config.Configuration import Configuration
from src.Infrastructure.interface.ICityStationProvider import ICityStationProvider


class CityStationProvider(ICityStationProvider):
    """
    Adapter concret qui lit un JSON et fournit les infos de mapping.


    """
    _instance = None

    def __new__(cls) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            config = Configuration()
            cls._instance._path = config.PATH_CONFIG_MAPPING
            cls._instance._mapping = cls._instance._load()
        return cls._instance

    def _load(self) -> Dict[str, Dict[str, str]]:
        with open(self._path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # normalisation en lower pour être plus tolérant
        normalized: Dict[str, Dict[str, str]] = {}
        for city, stations in data.items():
            city_key = city.lower()
            normalized[city_key] = {k.lower(): v for k, v in stations.items()}
        return normalized

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
