# src/config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()


class Configuration:
    API_BASE_URL: str = os.getenv("API_BASE_URL", "")
    API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "10"))
    API_RECORDS_URL: str = os.getenv("API_RECORDS_URL", "")
    PATH_CONFIG_MAPPING: str = os.getenv("PATH_CONFIG_MAPPING", "")
    API_OPTIONS_URL: str = os.getenv("API_OPTIONS_URL", "")

    if not API_BASE_URL:
        raise ValueError(
            "La variable d'environnement API_BASE_URL est manquante")
