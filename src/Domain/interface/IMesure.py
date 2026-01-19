"""IMesure domain interface module."""
from abc import ABC, abstractmethod

class IMesure(ABC):
    """Interface for mesure classes."""
    @abstractmethod
    def get_value(self) -> float:
        """Gets the value."""

    @abstractmethod
    def get_unit(self) -> str:
        """Gets the unit."""