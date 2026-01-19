"""JSONDataExtractor infrastructure module."""
from infrastructure.interface.IDataExtractor import IDataExtractor
import json
from pathlib import Path

class JSONExtractor(IDataExtractor):
    """
    Extracts data from a local JSON file.
    """

    def __init__(self, json_path: str | Path):
        """Initializes the instance."""
        self.json_path = Path(json_path)

    def extract(self, limit: int=200) -> dict[str, any]:
        """Performs extract."""
        if not self.json_path.exists():
            raise FileNotFoundError(f'Fichier JSON introuvable : {self.json_path}')
        with self.json_path.open('r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data[:limit]
        elif isinstance(data, dict):
            return [data]
        else:
            raise ValueError('Le fichier JSON n’a pas un format attendu (liste ou dict)')