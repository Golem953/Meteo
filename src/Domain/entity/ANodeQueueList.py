"""ANodeQueueList domain module."""
from domain.interface.INode import INode

class ANodeQueueList(INode):
    """class for queue list structures."""

    def __init__(self, value, next_node=None):
        """Initializes the instance."""
        self._value = value
        self._next = next_node

    def get_value(self):
        """Gets the value."""
        return self._value

    def get_next(self):
        """Gets the next."""
        return self._next

    def set_next(self, next_node):
        """Sets the next."""
        self._next = next_node

    def __repr__(self):
        """Returns a string representation of the instance."""
        return f'Node({self._value})'