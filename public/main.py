# public/main.py

from src.Application.builder.CityBuilder import CityBuilder

def main():
    """
    Point d’entrée de l’application.
    Construit les villes à partir d’un CityBuilder,
    puis affiche ou exploite les résultats.
    """

    # Liste des villes que l’on veut construire
    city_names = [
        "Toulouse",
    ]

    # Liste des stations (ou identifiants de station)
    # Ex: ["compans", "purpan", "cugnaux"]
    list_of_stations = [
        "Compans Cafarelli",
    ]

    # On instancie le CityBuilder
    builder = CityBuilder(
        names=city_names,
        list_of_stations=list_of_stations
    )

    # On construit toutes les villes
    cities = builder.build()

    # TEST : on les affiche
    for name, city in cities.items():
        print(f"=== Ville : {name.upper()} ===")
        print(f"Nombre de stations : {len(city.stations)}")

        for station in city.stations:
            print(f"  - Station : {station.name}")
            print(f"    Nombre de records : {len(station.records)}")
            print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
