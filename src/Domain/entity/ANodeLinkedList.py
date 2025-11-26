class ANodeLinkedList:
    def __init__(self, value, next_node=None):
        self.valeur = value
        self.suivant = next_node

    def get_value(self):
        return self.valeur

    def get_next(self):
        return self.suivant

    def set_next(self, next_node):
        self.suivant = next_node