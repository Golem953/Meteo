from Domain.ports.IDataExtractor import IDataExtractor
import json
from pathlib import Path
from typing import Any, List, Dict


class JSONExtractor(IDataExtractor):
    """
    Extrait des données depuis un fichier JSON local.
    """
    def __init__(self, json_path: str | Path):
        self.json_path = Path(json_path)

    def extract(self, limit: int = 200) -> List[Dict[str, Any]]:
        if not self.json_path.exists():
            raise FileNotFoundError(f"Fichier JSON introuvable : {self.json_path}")

        with self.json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        # On limite si c'est une liste d'enregistrements
        if isinstance(data, list):
            return data[:limit]
        elif isinstance(data, dict):
            # Si c’est un gros dict, tu peux ajuster ici selon ton schéma
            return [data]
        else:
            raise ValueError("Le fichier JSON n’a pas un format attendu (liste ou dict)")