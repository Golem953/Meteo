from dataclasses import dataclass
from typing import Dict, List, Any
from ..Infrastructure.Extractor.JSONExtractor import JSONExtractor
from ..Infrastructure.Analyzers.ColumnDropper import ColumnDropper


class GetFilteredWeatherData:
    """
    Cas d’usage unique :
    - extrait les données météo depuis un fichier JSON
    - supprime les colonnes demandées
    """

    def execute(self, inp: GetFilteredWeatherDataInput) -> List[Dict[str, Any]]:
        # 1️⃣ Extraire les données JSON
        extractor = JSONExtractor(inp.json_path)
        data = extractor.extract()

        # 2️⃣ Supprimer les colonnes spécifiées
        dropper = ColumnDropper(data)
        filtered = dropper.drop_columns(inp.columns_to_drop)

        # 3️⃣ Retourner le résultat
        return filtered