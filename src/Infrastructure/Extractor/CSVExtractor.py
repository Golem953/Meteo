from src.Domain.Interfaces.IExtractor import IExtractor
import csv
from pathlib import Path
from typing import Any, List, Dict


class CSVExtractor(IExtractor):
    """
    Implémentation d'IExtractor pour extraire les données d'un fichier CSV local.
    """
    def __init__(self, csv_path: str | Path):
        self.csv_path = Path(csv_path)

    def extract(self, limit: int = 200) -> List[Dict[str, Any]]:
        if not self.csv_path.exists():
            raise FileNotFoundError(f"Le fichier CSV '{self.csv_path}' est introuvable.")

        with self.csv_path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = [row for _, row in zip(range(limit), reader)]

        return data
