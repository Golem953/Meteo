from src.Domain.entity.ARecord import ARecord


class AStation:
    def __init__(self, name: str, file_name: str, list_of_records: None|list[ARecord]):
        self.name = name
        self.file_name = file_name
        self.list_of_records = list_of_records
    
    def set_list_of_records(self, list_of_records: list[ARecord]):
        self.list_of_records = list_of_records