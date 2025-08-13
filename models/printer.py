# models/printer.py

from icmplib import ping
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

    def is_available(self,  timeout: float = 2.0) -> bool:
        """Prüft die Netzwerkverfügbarkeit des Druckers."""
        try:
            host = ping(self.dns, count=2, timeout=timeout)
            return host.is_alive
        
        except Exception as e:
            return False

    def to_dict(self) -> Dict[str, Any]:
        """Serialisiert das Objekt in ein Dictionary."""
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Printer":
        """Erstellt ein Objekt aus einem Dictionary."""
        return cls(**data)
