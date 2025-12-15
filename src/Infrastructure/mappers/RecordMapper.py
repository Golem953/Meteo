# src/meteo_app/infrastructure/mappers/record_mapper.py
from typing import Any, Dict, List

from Infrastructure.factory.MesureFactory import MesureFactory
# from ...domain.interface import IDataMapper
from src.Domain.entity.ARecord import ARecord
from src.Infrastructure.interface.IMappers import IMappers  # ta classe Record métier



class RecordMapper(IMappers):
    """
    Mappe les résultats JSON extraits (liste de mesures météo)
    vers une liste d'objets ARecord du domaine.
    """

    def __init__(self):
        self.mesure_factory = MesureFactory()

    def to_object(self, data: Dict[str, Any]) -> List[ARecord]:
        """
        data : dict complet du JSON (avec "results": [ ... ])
        Retourne une liste d'objets ARecord
        """

        

        records: List[ARecord] = []
        for item in data.get("results", []):
            try:
                record = ARecord(
                    id=int(item.get("id", 0)),
                    paris_date=item.get("heure_de_paris"),
                    temperature=self.mesure_factory.get_mesure("temperature", float(item.get("temperature_en_degre_c", 0.0))),
                    humidity=self.mesure_factory.get_mesure("humidity", float(item.get("humidite", 0.0))),
                    # conversion Pa -> hPa
                    pressure=self.mesure_factory.get_mesure("pressure", int(item.get("pression", 0)) // 100),
                )
                records.append(record)
            except Exception as e:
                # on ignore ou on log les entrées invalides
                print(f"⚠️ Erreur de mapping sur l'item {item}: {e}")
        return records
