from typing import  Protocol

class IDataExtractor(Protocol):
    def extract(self, limit):
        pass
        
