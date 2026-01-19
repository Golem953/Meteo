"""LinkedList infrastructure module."""
from domain.entity.ANodeLinkedList import ANodeLinkedList
from infrastructure.interface.IDataStructure import IDataStructure

class LinkedList(IDataStructure):

    """class for linked list data structure."""

    def __init__(self, first_node: ANodeLinkedList):
        """Initializes the instance."""
        self.first_node = first_node

    def add_node(self, first_node: ANodeLinkedList):
        """Performs add node."""
        self.get_last().set_next(first_node)

    def remove_node(self, value: str) -> bool:
        """Performs remove node."""
        if self.first_node is None:
            return False
        if self.first_node.get_value() == value:
            self.first_node = self.first_node.get_next()
            return True
        prev = self.first_node
        current = self.first_node.get_next()
        while current is not None:
            if current.get_value() == value:
                prev.set_next(current.get_next())
                return True
            prev = current
            current = current.get_next()
        return False

    def get_last(self):
        """Gets the last."""
        actual_node = self.first_node
        while actual_node.get_next() is not None:
            actual_node = actual_node.get_next()
        return actual_node

    def afficher_liste(self):
        """Performs afficher liste."""
        maillon_actuel = self.first_node
        while maillon_actuel.get_next() is not None:
            maillon_actuel = maillon_actuel.get_next()
        print(maillon_actuel.get_value() + '-> Next' + str(maillon_actuel.get_next()) + '||')

    def __str__(self):
        """Returns a string representation of the instance."""
        actual_node = self.first_node
        return_string = ''
        while actual_node.get_next() is not None:
            return_string += str(actual_node.get_value()) + ' -> '
            actual_node = actual_node.get_next()
        return return_string