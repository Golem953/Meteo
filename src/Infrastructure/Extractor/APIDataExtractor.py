"""APIDataExtractor infrastructure module."""
from domain.config.Configuration import Configuration
from infrastructure.interface.IDataExtractor import IDataExtractor
from infrastructure.http.APIClient import APIClient

class APIDataExtractor(IDataExtractor):

    def __init__(self, config: Configuration) -> None:
        """Initializes the instance."""
        self.client = APIClient(config)

    def extract(self, file_name: str, limit: int=200) -> dict[str, any]:
        """Performs extract."""
        data = self.client.call(limit, file_name)
        return data