from src.Infrastructure.api_client import APIClient
from src.Domain.Interfaces.IExtractor import IExtractor

class APIExtractor(IExtractor):
    def __init__(self, client: APIClient | None = None):
        self.client = client or APIClient()

    def extract(self, limit: int = 200):
        data = self.client.fetch_records(limit)
        return data