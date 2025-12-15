from asyncio import Protocol

from Domain.entity.ACity import ACity
from abc import ABC, abstractmethod

class IBuilder(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def build(self) -> dict[str, ACity]:
        pass
