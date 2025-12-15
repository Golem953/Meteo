from Domain.config.Configuration import Configuration
from Infrastructure.interface.IDataExtractor import IDataExtractor
from src.Infrastructure.http.APIClient import APIClient


class APIDataExtractor(IDataExtractor):

    def __init__(self, config: Configuration) -> None:

        self.client =  APIClient(config)

    def extract(self,file_name: str, limit: int = 200) -> dict[str, any]:
        
        data = self.client.call(limit, file_name)
        return data
