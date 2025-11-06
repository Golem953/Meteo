# src/config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_BASE_URL: str = os.getenv("API_BASE_URL", "")
    API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "10"))

    if not API_BASE_URL:
        raise ValueError("La variable d'environnement API_BASE_URL est manquante")
