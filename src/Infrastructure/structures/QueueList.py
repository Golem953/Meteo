"""QueueList infrastructure module."""
from infrastructure.interface.IDataStructure import IDataStructure
from domain.entity.ANodeQueueList import ANodeQueueList

class QueueList(IDataStructure):
    """
    Queue (FIFO) implemented using a simple Python list.
    Uses append() for enqueue and pop(0) for dequeue/remove.
    """

    def __init__(self, first_node: ANodeQueueList):
        """Initializes the instance."""
        self.first_node = first_node
        self._items: list[ANodeQueueList] = [self.first_node]

    def add_node(self, value: ANodeQueueList):
        """Add a value at the end of the queue (FIFO)."""
        self._items[len(self._items) - 1].set_next(value)
        self._items.append(value)

    def remove_node(self) -> bool:
        """Remove the first matching value from the queue. Returns True if removed, False otherwise."""
        try:
            self._items.pop(0)
            return True
        except IndexError:
            return False