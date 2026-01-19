

from domain.entity.ACity import ACity
from abc import ABC, abstractmethod


class IBuilder(ABC):
    """Interface for builder classes."""

    @abstractmethod
    def build(self) -> dict[str, ACity]:
        """Builds the object."""
