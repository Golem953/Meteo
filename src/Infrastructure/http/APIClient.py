"""APIClient infrastructure module."""
import requests
from domain.config.Configuration import Configuration

class APIClient:
    """Client for interacting with weather API."""

    def __init__(self, config: Configuration):
        """Initializes the instance."""
        self.base_url = config.API_BASE_URL.rstrip('/')
        self.records_url = config.API_RECORDS_URL.rstrip('/')
        self.timeout = config.API_TIMEOUT
        self.session = requests.Session()
        self.options_url = config.API_OPTIONS_URL

    def call(self, limit: int, file_name: str='') -> dict:
        """Performs call."""
        url = f'{self.base_url}/{file_name}/{self.options_url}&limit={limit}'
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()