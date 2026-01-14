"""IMappers infrastructure interface module."""
from typing import Any, Dict, List
from abc import ABC, abstractmethod

class IMappers(ABC):

    @abstractmethod
    def to_object(self, data: Dict[str, Any]) -> object | List[object]:
        """Performs to object."""