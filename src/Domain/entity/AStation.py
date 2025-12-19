"""AStation entity module."""

from domain.entity.ARecord import ARecord


class AStation:
    """Abstract class representing a weather station."""

    def __init__(
        self, name: str, file_name: str, list_of_records: None | list[ARecord]
    ):
        """Initializes the instance."""
        self.name = name
        self.file_name = file_name
        self.list_of_records = list_of_records

    def set_list_of_records(self, list_of_records: list[ARecord]):
        """Sets the list of records."""
        self.list_of_records = list_of_records
