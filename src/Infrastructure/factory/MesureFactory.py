from src.Domain.entity.ATemperature import ATemperature
from src.Domain.entity.AHumidity import AHumidity
from src.Domain.entity.APressure import APressure

class MesureFactory():
    
    def __init__(self) -> None:
        pass

    def get_mesure(self, mesure_type: str, valeur: float):
        if mesure_type == "temperature":
            return ATemperature(valeur,"°C")
        elif mesure_type == "humidity":
            return AHumidity(valeur,"%")
        elif mesure_type == "pressure":
            return APressure(valeur,"Pa")
        else:
            raise ValueError(f"Unknown mesure type: {mesure_type}")