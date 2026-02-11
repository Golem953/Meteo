"""Station entity module."""

from domain.entity.record import Record


class Station:
    """class representing a weather station."""

    def __init__(
        self, name: str, file_name: str, list_of_records: None | list[Record]
    ):
        """Initializes the instance."""
        self.name = name
        self.file_name = file_name
        self.list_of_records = list_of_records

    def set_list_of_records(self, list_of_records: list[Record]):
        """Sets the list of records."""
        self.list_of_records = list_of_records
