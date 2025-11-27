class ANodeLinkedList:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        # print("1 "+str(self.value))
        # print("2 "+str(self.next_node))
        self.next_node = next_node