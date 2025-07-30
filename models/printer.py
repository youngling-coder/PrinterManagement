# models/printer.py

import socket
from typing import Dict, Any


class Printer:
    def __init__(
        self, dns: str, name: str, model: str, driver_name: str, driver_inf_path: str
    ):
        self.dns = dns
        self.name = name
        self.model = model
        self.driver_name = driver_name
        self.driver_inf_path = driver_inf_path

    def is_available(self, port: int = 80, timeout: float = 1.0) -> bool:
        """Prüft die Netzwerkverfügbarkeit des Druckers."""
        try:
            with socket.create_connection((self.dns, port), timeout=timeout):
                return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

    def to_dict(self) -> Dict[str, Any]:
        """Serialisiert das Objekt in ein Dictionary."""
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Printer":
        """Erstellt ein Objekt aus einem Dictionary."""
        return cls(**data)
