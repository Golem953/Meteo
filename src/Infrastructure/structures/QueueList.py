
from src.Domain.ports.IDataStructure import IDataStructure, T
from src.Domain.entity.ANodeQueueList import ANodeQueueList

class QueueList(IDataStructure):
    """
    Queue (FIFO) implemented using a simple Python list.
    Uses append() for enqueue and pop(0) for dequeue/remove.
    """

    def __init__(self):
        self._items: list[ANodeQueueList] = []

    # -----------------------------------
    #              ADD (ENQUEUE)
    # -----------------------------------
    def add_node(self, value: ANodeQueueList) -> None:
        """Add a value at the end of the queue (FIFO)."""
        self._items.append(value)

    def remove_node(self) -> bool:
        """Remove the first matching value from the queue. Returns True if removed, False otherwise."""
        try:
            self._items.pop(0)
            return True
        except IndexError:
            return False
