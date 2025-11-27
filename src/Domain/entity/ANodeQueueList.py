from src.Domain.ports.INode import INode

class ANodeQueueList(INode):
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    # -------------------------
    #       INTERFACE METHODS
    # -------------------------
    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

    # -------------------------
    #        UTILE (optionnel)
    # -------------------------
    def __repr__(self):
        return f"Node({self._value})"
