from asyncio import Protocol


class IBuilder(Protocol):
    def __init__(self):
        pass
        

    def build(self):
       pass