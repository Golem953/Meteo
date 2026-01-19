"""
Entry point of the weather application.

Examples:
  py .\\__main__.py -c "toulouse, paris" -s "compans cafarelli, universite paul sabatier"
"""

from __future__ import annotations
import argparse
import os
import sys
from typing import List


def _ensure_project_on_syspath():
    """Adds the project folder to sys.path to allow 'src.*' imports."""
    root_dir = os.path.dirname(__file__)
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)


def _parse_comma_separated(value: str) -> List[str]:
    """Parse 'a, b, c' -> ['a', 'b', 'c'] (trim + remove empties)."""
    return [v.strip() for v in value.split(",") if v.strip()]


def _parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        prog="meteo", description="Launch the weather app with cities and stations."
    )
    parser.add_argument(
        "--city",
        "-c",
        type=_parse_comma_separated,
        default="toulouse",
        help='Cities separated by commas (ex: -c "toulouse, paris")',
    )
    parser.add_argument(
        "--stations",
        "-s",
        type=_parse_comma_separated,
        default="compans cafarelli, universite paul sabatier",
        help='Stations separated by commas (ex: -s "compans cafarelli, universite paul sabatier")',
    )
    return parser.parse_args()


def main():
    """Entry point."""
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
