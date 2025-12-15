from abc import ABC, abstractmethod

class INode(ABC):
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def set_next(self, next_node):
        pass
