

from domain.entity.city import City
from abc import ABC, abstractmethod


class IBuilder(ABC):
    """Interface for builder classes."""

    @abstractmethod
    def build(self) -> dict[str, City]:
        """Builds the object."""
