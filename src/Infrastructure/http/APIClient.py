# src/infrastructure/api_client.py
import requests
from src.Domain.configuration import configuration


class APIClient:
    def __init__(
        self, base_url: str = configuration.API_BASE_URL, records_url: str = configuration.API_RECORDS_URL, timeout: int = configuration.API_TIMEOUT
    ):
        self.base_url = base_url.rstrip("/")
        self.records_url = records_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.options_url = configuration.API_OPTIONS_URL

    def extract(self, limit: int, file_name: str = "") -> dict:
        # url = f"{self.records_url}&limit={limit}"
        url = f"{self.base_url}/{file_name}/{self.options_url}&limit={limit}"
        
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()