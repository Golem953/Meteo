from src.Domain.entity.ARecord import ARecord


class AStation:
    def __init__(self, name: str, list_of_records: list[ARecord]):
        self.name = name
        self.list_of_records = list_of_records    