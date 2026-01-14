"""IDataExtractor infrastructure interface module."""
from abc import ABC, abstractmethod

class IDataExtractor(ABC):

    @abstractmethod
    def extract(self, limit: int) -> dict[str, any]:
        """Performs extract."""