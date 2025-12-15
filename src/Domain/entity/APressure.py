

from Domain.interface.IMesure import IMesure


class APressure(IMesure):
    
    def __init__(self, value: float, unit: str) -> None:
        self.value = value
        self.unit = unit

    def get_value(self) -> float:
        return self.value

    def get_unit(self) -> str:
        return self.unit