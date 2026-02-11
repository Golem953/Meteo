"""APIDataExtractor infrastructure module."""
from domain.config.configuration import Configuration
from infrastructure.interface.idata_extractor import IDataExtractor
from infrastructure.http.api_client import APIClient

class APIDataExtractor(IDataExtractor):

    """Abstract base class for extracting data from APIs."""

    def __init__(self, config: Configuration) -> None:
        """Initializes the instance."""
        self.client = APIClient(config)

    def extract(self, file_name: str, limit: int=200) -> dict[str, any]:
        """Performs extract."""
        data = self.client.call(limit, file_name)
        return data