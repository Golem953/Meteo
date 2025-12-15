import sys
import os

ROOT_DIR = os.path.dirname(__file__)  # ...\Meteo
sys.path.append(ROOT_DIR)


from src.Application.builder.CityBuilder import CityBuilder

from src.Infrastructure.provider.CityStationConfigMemoryProvider import (
    CityStationConfigMemoryProvider,
)


def main() -> int:
    city_names = ["toulouse"]
    city_station = [
        "compans cafarelli",
        "universite paul sabatier",
    ]

    provider = CityStationConfigMemoryProvider()

    # builder = CityBuilder(
    #     names_city=city_names,
    #     stations_choose=city_station,
    #     city_station_provider=provider,
    # )

    cities_builder = (
        CityBuilder()
        .set_names_city(city_names)
        .set_stations_choose(city_station)
        .set_city_station_provider(provider)
        .build()
    )

    # print(cities["toulouse"].stations[0].name)
    # exit(0)

    for name, city in cities_builder.items():
        print(f"=== {name.upper()} ===")
        for station in city.stations:
            print(f"- Station: {station.name} ({len(station.list_of_records)} records)")
            print("  Records:")
            for record in station.list_of_records:
                print(
                    f"    - Date: {record.paris_date}, Temp: {record.temperature}°C, Humidity: {record.humidity}%, Pression: {record.pressure}Pa"
                )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
