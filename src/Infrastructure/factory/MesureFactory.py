"""MesureFactory infrastructure module."""
from domain.entity.ATemperature import ATemperature
from domain.entity.AHumidity import AHumidity
from domain.entity.APressure import APressure

class MesureFactory:

    def __init__(self) -> None:
        """Initializes the instance."""
        pass

    def get_mesure(self, mesure_type: str, valeur: float):
        """Gets the mesure."""
        if mesure_type == 'temperature':
            return ATemperature(valeur, '°C')
        elif mesure_type == 'humidity':
            return AHumidity(valeur, '%')
        elif mesure_type == 'pressure':
            return APressure(valeur, 'Pa')
        else:
            raise ValueError(f'Unknown mesure type: {mesure_type}')