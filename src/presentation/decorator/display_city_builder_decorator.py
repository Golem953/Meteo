"""DisplayCityBuilderDecorator presentation module."""

from application.builder.city_builder import CityBuilder
from domain.entity.city import City
from infrastructure.provider import city_station_config_memory_provider


class DisplayCityBuilderDecorator:

    """Decorator for CityBuilder that displays city building information."""

    def __init__(
        self,
        city_name: list[str],
        city_stations: list[str],
        city_station_provider: city_station_config_memory_provider,
        city_builder: CityBuilder,
    ):
        """Initializes the instance."""
        self.city_name = city_name
        self.city_stations = city_stations
        self.city_builder = city_builder
        self.city_station_provider = city_station_provider

    def show(self):
        """Performs show."""
        city_builder: dict[str, City] = (
            CityBuilder()
            .set_names_city(self.city_name)
            .set_stations_choose(self.city_stations)
            .set_city_station_provider(self.city_station_provider)
            .build()
        )
        for name, city in city_builder.items():
            print(f"=== {name.upper()} ===")
            for station in city.stations:
                print(
                    f"- Station: {station.name} ({len(station.list_of_records)} records)"
                )
                print("  Records:")
                for record in station.list_of_records:
                    print(
                        f"    - Date: {record.paris_date}, Temp: {record.temperature.get_value()}°C, Humidity: {record.humidity.get_value()}%, Pression: {record.pressure.get_value()}Pa"
                    )
