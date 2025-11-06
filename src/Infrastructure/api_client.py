# src/infrastructure/api_client.py
import requests
from src.config.Settings import Settings


class APIClient:
    def __init__(
        self, base_url: str = Settings.API_BASE_URL, timeout: int = Settings.API_TIMEOUT
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def fetch_records(self, limit: int):
        url = f"{self.base_url}/records?limit={limit}"
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
