"""ANodeLinkedList entity module."""
from domain.interface.INode import INode

class ANodeLinkedList(INode):
    """class for linked list structures."""

    def __init__(self, value, next_node=None):
        """Initializes the instance."""
        self.value = value
        self.next_node = next_node

    def get_value(self):
        """Gets the value."""
        return self.value

    def get_next(self):
        """Gets the next."""
        return self.next_node

    def set_next(self, next_node):
        """Sets the next."""
        self.next_node = next_node