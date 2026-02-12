from infrastructure.factory.mesure_factory import MesureFactory
from domain.entity.temperature import Temperature
from domain.entity.humidity import Humidity
from domain.entity.pressure import Pressure


import pytest


test_data = [
  ("temperature", 25.0,Temperature(25.0, '°C')),
  ("humidity", 60.0, Humidity(60.0, '%')),
  ("pressure", 1013.25, Pressure(1013.25, 'Pa'))
] 
@pytest.mark.parametrize("a, b, expected", test_data) 
def test_mesure_factory_get_mesure(a, b, expected):
  assert MesureFactory().get_mesure(a, b) == expected


def test_mesure_factory_unknown_type():
    with pytest.raises(ValueError):
        MesureFactory().get_mesure("wind", 10.0)

def test_mesure_factory_unknown_type_message():
    with pytest.raises(ValueError, match="Unknown mesure type"):
        MesureFactory().get_mesure("wind", 10.0)

