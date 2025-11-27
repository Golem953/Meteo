from Domain.ports.IDataExtractor import IDataExtractor
from src.Infrastructure.http.APIClient import APIClient


class APIDataExtractor(IDataExtractor):
    def __init__(self, client: APIClient | None = None):
        self.client = client or APIClient()

    def extract(self, limit: int = 200) -> dict[str, any]:
        data = self.client.fetch_records(limit)
        return data
