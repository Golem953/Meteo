"""Configuration domain module."""
import os
from dotenv import load_dotenv
from typing import Optional
load_dotenv()

class Configuration:
    _instance: Optional['Configuration'] = None

    def __new__(cls):
        """Performs   new  ."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance

    def _load(self) -> None:
        """Performs  load."""
        self.API_BASE_URL: str = os.getenv('API_BASE_URL', '')
        self.API_TIMEOUT: int = int(os.getenv('API_TIMEOUT', '10'))
        self.API_RECORDS_URL: str = os.getenv('API_RECORDS_URL', '')
        self.PATH_CONFIG_MAPPING: str = os.getenv('PATH_CONFIG_MAPPING', '')
        self.API_OPTIONS_URL: str = os.getenv('API_OPTIONS_URL', '')
        if not self.API_BASE_URL:
            raise ValueError("La variable d'environnement API_BASE_URL est manquante")