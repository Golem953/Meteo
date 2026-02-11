"""QueueList infrastructure module."""
from infrastructure.interface.idata_structure import IDataStructure
from domain.entity.node_queue_list import NodeQueueList

class QueueList(IDataStructure):
    """
    Queue (FIFO) implemented using a simple Python list.
    Uses append() for enqueue and pop(0) for dequeue/remove.
    """

    def __init__(self, first_node: NodeQueueList):
        """Initializes the instance."""
        self.first_node = first_node
        self._items: list[NodeQueueList] = [self.first_node]

    def add_node(self, value: NodeQueueList):
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