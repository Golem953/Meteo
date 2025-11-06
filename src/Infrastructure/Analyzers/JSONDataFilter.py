# src/Infrastructure/Analyzers/DataFilter.py

import json;

class DataFilter:
    
    def __init__(self, data: json):
        self.data = data

    def filter_meteo(self, filter_params: dict) -> json:

        
        return [
            d for d in self.data
            if (
                -10 <= float(d.get("temperature_en_degre_c", 0)) < 50
                and 90000 < float(d.get("pression", 0)) < 110000
                and 0 < float(d.get("humidite", 0)) < 105
            )
        ]
