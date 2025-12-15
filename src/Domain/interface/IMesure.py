from abc import ABC, abstractmethod

class IMesure(ABC):

    @abstractmethod
    def get_value(self) -> float:
        pass

    @abstractmethod
    def get_unit(self) -> str:
        pass
