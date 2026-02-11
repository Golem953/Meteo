"""MesureFactory infrastructure module."""
from domain.entity.temperature import Temperature
from domain.entity.humidity import Humidity
from domain.entity.pressure import Pressure

class MesureFactory:
    """Factory class for creating measurement objects."""

    def __init__(self) -> None:
        """Initializes the instance."""
        pass

    def get_mesure(self, mesure_type: str, valeur: float) -> Humidity | Pressure | Temperature:
        """Gets the mesure."""
        if mesure_type == 'temperature':
            return Temperature(valeur, '°C')
        elif mesure_type == 'humidity':
            return Humidity(valeur, '%')
        elif mesure_type == 'pressure':
            return Pressure(valeur, 'Pa')
        else:
            raise ValueError(f'Unknown mesure type: {mesure_type}')