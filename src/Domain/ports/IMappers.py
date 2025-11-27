from typing import Any, Dict, List, Protocol

from abc import ABC, abstractmethod
class IMappers(ABC):

    @abstractmethod
    def to_object(self, data: Dict[str, Any]) -> object | List[object]:
        pass
