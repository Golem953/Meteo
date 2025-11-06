# public/index.py
from __future__ import annotations
import sys
from pathlib import Path

# 👉 Ajoute la racine du projet (dossier qui contient `public/` et `src/`) au sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# Imports du projet (fonctionneront même si tu lances depuis public/)
from src.Infrastructure.Extractor.APIExtractor import APIExtractor
from src.Infrastructure.Extractor.CSVExtractor import CSVExtractor
from src.Infrastructure.Extractor.JSONExtractor import JSONExtractor


if __name__ == "__main__":
    # extractor = APIExtractor()
    # data = extractor.extract(limit=10)
    # print(data)
    # extractor = CSVExtractor("data/42-station-meteo-toulouse-parc-compans-cafarelli.json")
    # data = extractor.extract(limit=100)
    # for row in data[:5]:
    #     print(row)
    extractor = JSONExtractor("src/Infrastructure/data/42-station-meteo-toulouse-parc-compans-cafarelli.json")
    data = extractor.extract(limit=50)
    print(data[:10])