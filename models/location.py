# models/location.py

from typing import List, Dict, Any
from .printer import Printer

class Location:
    def __init__(self, name: str, printers: List[Printer] = None):
        self.name = name
        self.printers = printers or []

    def get_printer_by_dns(self, dns: str) -> Printer | None:
        """Sucht einen Drucker anhand seines DNS-Namens."""
        for printer in self.printers:
            if printer.dns == dns:
                return printer
        return None

    def add_printer(self, printer: Printer):
        """Fügt einen Drucker hinzu, wenn der DNS-Name noch nicht existiert."""
        if not self.get_printer_by_dns(printer.dns):
            self.printers.append(printer)
        else:
            raise ValueError(f"Ein Drucker mit dem DNS-Namen {printer.dns} existiert bereits an diesem Standort.")

    def remove_printer(self, dns: str):
        """Entfernt einen Drucker anhand seines DNS-Namens."""
        printer_to_remove = self.get_printer_by_dns(dns)
        if printer_to_remove:
            self.printers.remove(printer_to_remove)
        else:
            raise ValueError(f"Drucker mit DNS {dns} nicht an diesem Standort gefunden.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialisiert das Objekt und seine Drucker in ein Dictionary."""
        return {
            "name": self.name,
            "printers": [printer.to_dict() for printer in self.printers]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Location":
        """Erstellt ein Objekt aus einem Dictionary."""
        printers = [Printer.from_dict(p_data) for p_data in data.get("printers", [])]
        return cls(name=data["name"], printers=printers)