"""IMappers infrastructure interface module."""
from typing import Any, Dict, List
from abc import ABC, abstractmethod

class IMappers(ABC):
    """Interface for data mapping classes."""

    @abstractmethod
    def to_object(self, data: Dict[str, Any]) -> object | List[object]:
        """Performs to object."""