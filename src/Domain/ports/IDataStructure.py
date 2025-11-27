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


    def add(self, value: T) -> None:
        """Add a value into the data structure."""
        pass


    @abstractmethod
    def search(self, value: T) -> bool:
        """Return True if the value exists in the data structure."""
        pass

    @abstractmethod
    def __iter__(self) -> Iterable[T]:
        """Return an iterator over the stored values."""
        pass
