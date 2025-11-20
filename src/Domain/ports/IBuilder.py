from asyncio import Protocol

from Domain.entity.ACity import ACity


class IBuilder(Protocol):
    def __init__(self):
        pass
        

    def build(self) -> dict[str, ACity]:
       pass