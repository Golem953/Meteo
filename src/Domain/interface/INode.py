"""INode domain interface module."""
from abc import ABC, abstractmethod

class INode(ABC):

    @abstractmethod
    def get_value(self):
        """Gets the value."""

    @abstractmethod
    def get_next(self):
        """Gets the next."""

    @abstractmethod
    def set_next(self, next_node):
        """Sets the next."""
