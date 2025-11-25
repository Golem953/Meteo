from typing import Any, Dict, List, Protocol


class IMappers(Protocol):

    def to_object(self, data: Dict[str, Any]) -> object | List[object]:
        pass
