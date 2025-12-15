# src/infrastructure/api_client.py
import requests
from src.Domain.config.Configuration import Configuration


class APIClient:
    def __init__(
        self, config: Configuration
    ):
        self.base_url = config.API_BASE_URL.rstrip("/")
        self.records_url = config.API_RECORDS_URL.rstrip("/")
        self.timeout = config.API_TIMEOUT
        self.session = requests.Session()
        self.options_url = config.API_OPTIONS_URL

    def call(self, limit: int, file_name: str = "") -> dict:
        # url = f"{self.records_url}&limit={limit}"
        url = f"{self.base_url}/{file_name}/{self.options_url}&limit={limit}"

        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
