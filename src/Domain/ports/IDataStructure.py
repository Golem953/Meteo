from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterable

T = TypeVar("T")
from abc import ABC, abstractmethod

class IDataStructure(ABC, Generic[T]):
    """
    Interface representing a generic data structure.
    It defines the contract for adding and searching elements.
    This interface contains NO implementation.
    """


    @abstractmethod
    def add_node(self, value: T) -> None:
        """Add a value into the data structure."""
        pass

    @abstractmethod
    def remove_node(self, value: T) -> None:
        """Remove a value from the data structure."""
        pass
