from typing import Protocol


class IDataExtractor(Protocol):
    def extract(self, limit: int) -> dict[str, any]:
        pass
