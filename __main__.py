"""
Point d'entrée de l'application meteo.

Exemples :
  py .\\__main__.py -c "toulouse, paris" -s "compans cafarelli, universite paul sabatier"
"""

from __future__ import annotations
import argparse
import os
import sys
from typing import List


def _ensure_project_on_syspath():
    """Ajoute le dossier du projet au sys.path pour permettre les imports 'src.*'."""
    root_dir = os.path.dirname(__file__)
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)


def _parse_comma_separated(value: str) -> List[str]:
    """Parse 'a, b, c' -> ['a', 'b', 'c'] (trim + suppression des vides)."""
    return [v.strip() for v in value.split(",") if v.strip()]


def _parse_args() -> argparse.Namespace:
    """Parse les arguments CLI."""
    parser = argparse.ArgumentParser(
        prog="meteo", description="Lance l'app météo avec villes et stations."
    )
    parser.add_argument(
        "--city",
        "-c",
        type=_parse_comma_separated,
        default="toulouse",
        help='Villes séparées par des virgules (ex: -c "toulouse, paris")',
    )
    parser.add_argument(
        "--stations",
        "-s",
        type=_parse_comma_separated,
        default="compans cafarelli, universite paul sabatier",
        help='Stations séparées par des virgules (ex: -s "compans cafarelli, universite paul sabatier")',
    )
    return parser.parse_args()


def main():
    """Point d'entrée."""
    _ensure_project_on_syspath()
    from presentation.decorator.DisplayCityBuilderDecorator import (
        DisplayCityBuilderDecorator,
    )
    from src.application.builder.CityBuilder import CityBuilder
    from src.infrastructure.provider.CityStationConfigMemoryProvider import (
        CityStationConfigMemoryProvider,
    )

    args = _parse_args()
    DisplayCityBuilderDecorator(
        city_name=args.city,
        city_stations=args.stations,
        city_station_provider=CityStationConfigMemoryProvider(),
        city_builder=CityBuilder(),
    ).show()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
