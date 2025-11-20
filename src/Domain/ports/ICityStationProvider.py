from typing import Protocol, List, Optional


class ICityStationProvider(Protocol):
    """
    Port d'accès au mapping ville -> stations -> fichier.

    Respecte ISP : interface très fine utilisée par l'application.
    """

    def get_stations_for_city(self, city: str) -> List[str]:
        """
        Ex: "toulouse" -> ["compans", "purpan", "ramonville"]
        """
        ...

    def get_file_for_station(self, station_key: str) -> Optional[str]:
        """
        Ex: "compans" -> "42-station-meteo-toulouse-parc-compans-cafarelli"
        Retourne None si la station n'existe pas.
        """
        ...
