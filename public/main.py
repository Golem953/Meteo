import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  
sys.path.append(ROOT_DIR)

from src.Application.builder.CityBuilder import CityBuilder
from src.Infrastructure.config.CityStationProvider import CityStationProvider

def main() -> int:
    city_names = ["toulouse"]

    provider = CityStationProvider()

    builder = CityBuilder(
        names=city_names,
        city_station_provider=provider,
    )

    cities = builder.build()

    # print(cities["toulouse"].stations[0].name)
    # exit(0)

    for name, city in cities.items():
        print(f"=== {name.upper()} ===")
        for station in city.stations:
            print(f"- Station: {station.name} ({len(station.list_of_records)} records)")
            print("  Records:")
            for record in station.list_of_records:
                print(f"    - Date: {record.paris_date}, Temp: {record.temperature}°C, Humidity: {record.humidity}%, Pression: {record.pressure}Pa") 



    return 0

if __name__ == "__main__":
    raise SystemExit(main())
