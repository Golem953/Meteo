"""RecordMapper infrastructure module."""
from typing import Any, Dict, List
from infrastructure.factory.MesureFactory import MesureFactory
from domain.entity.ARecord import ARecord
from infrastructure.interface.IMappers import IMappers

class RecordMapper(IMappers):
    """
    Maps the extracted JSON results (list of weather measurements)
    to a list of ARecord objects.
    """

    def __init__(self):
        """Initializes the instance."""
        self.mesure_factory = MesureFactory()

    def to_object(self, data: Dict[str, Any]) -> List[ARecord]:
        """
        data : dict complet du JSON (avec "results": [ ... ])
        Retourne une liste d'objets ARecord
        """
        records: List[ARecord] = []
        for item in data.get('results', []):
            try:
                record = ARecord(id=int(item.get('id', 0)), paris_date=item.get('heure_de_paris'), temperature=self.mesure_factory.get_mesure('temperature', float(item.get('temperature_en_degre_c', 0.0))), humidity=self.mesure_factory.get_mesure('humidity', float(item.get('humidite', 0.0))), pressure=self.mesure_factory.get_mesure('pressure', int(item.get('pression', 0)) // 100))
                records.append(record)
            except Exception as e:
                print(f"⚠️ Erreur de mapping sur l'item {item}: {e}")
        return records