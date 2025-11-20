from typing import Any, Dict, List, Protocol
from src.Domain.entity.ARecord import ARecord


class IMappers(Protocol):

    def to_object(self, data: Dict[str, Any]) -> List[ARecord]:
        pass
