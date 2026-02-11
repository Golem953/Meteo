"""IDataExtractor infrastructure interface module."""
from abc import ABC, abstractmethod

class IDataExtractor(ABC):
    """Interface for data extraction classes."""

    @abstractmethod
    def extract(self, limit: int) -> dict[str, any]:
        """Performs extract."""