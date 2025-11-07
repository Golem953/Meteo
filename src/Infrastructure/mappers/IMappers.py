from typing import Any, Dict, List
from src.Domain.ARecord import ARecord


class IMappers:

    def to_object(self, data: Dict[str, Any]) -> List[ARecord]:
        pass
