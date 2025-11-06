# src/Infrastructure/Analyzers/ColumnDropper.py
from typing import List, Dict, Any

class ColumnDroppers:
    """
    Supprime des colonnes d'une liste d'enregistrements JSON selon un dictionnaire.
    Exemple :
        params = {"id": True, "humidite": True}
        data = ColumnDropper(data).drop_columns(params)
    """

    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data

    def drop_columns(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Supprime les colonnes dont le nom est une clé dans params.
        Peu importe la valeur (True, False, etc.) : la clé suffit.
        """
        if not isinstance(params, dict):
            raise TypeError("Les paramètres doivent être un dictionnaire (ex: {'colonne': True})")

        to_drop = set(params.keys())

        cleaned = [
            {k: v for k, v in row.items() if k not in to_drop}
            for row in self.data
        ]
        return cleaned
