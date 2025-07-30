# services/printer_service.py

from typing import List, Dict, Any
from data.storage import Storage
from models.location import Location
from models.printer import Printer


# Benutzerdefinierte Exceptions für klarere Fehlerbehandlung in den Views
class ItemNotFoundError(Exception):
    pass


class LocationNotEmptyError(Exception):
    pass


class PrinterService:
    def __init__(self, storage: Storage):
        self._storage = storage
        self._locations: List[Location] = []
        self.load_data()

    def _commit(self):
        """Schreibt den aktuellen Zustand der Daten in die Datei."""
        data_to_save = {
            loc.name: [p.to_dict() for p in loc.printers] for loc in self._locations
        }
        self._storage.save_data(data_to_save)

    def load_data(self):
        """Lädt die Daten aus dem Storage und wandelt sie in Model-Objekte um."""
        raw_data = self._storage.load_data()
        self._locations = []
        for loc_name, printers_data in raw_data.items():
            printers = [Printer.from_dict(p_data) for p_data in printers_data]
            self._locations.append(Location(name=loc_name, printers=printers))

    def get_all_locations(self) -> List[Location]:
        return self._locations

    def get_location_by_name(self, name: str) -> Location | None:
        for loc in self._locations:
            if loc.name == name:
                return loc
        return None

    def get_printer_by_dns(self, dns: str) -> tuple[Printer, Location] | None:
        for loc in self._locations:
            for printer in loc.printers:
                if printer.dns == dns:
                    return printer, loc
        return None

    def add_location(self, name: str):
        if self.get_location_by_name(name):
            raise ValueError(f"Standort '{name}' existiert bereits.")
        self._locations.append(Location(name=name))
        self._commit()

    def remove_location(self, name: str):
        location = self.get_location_by_name(name)
        if not location:
            raise ItemNotFoundError(f"Standort '{name}' nicht gefunden.")
        if location.printers:
            raise LocationNotEmptyError(
                f"Standort '{name}' enthält noch Drucker und kann nicht gelöscht werden."
            )
        self._locations.remove(location)
        self._commit()

    def add_printer_to_location(self, printer_data: Dict[str, Any], location_name: str):
        location = self.get_location_by_name(location_name)
        if not location:
            raise ItemNotFoundError(f"Standort '{location_name}' nicht gefunden.")
        if self.get_printer_by_dns(printer_data["dns"]):
            raise ValueError(
                f"Ein Drucker mit dem DNS '{printer_data['dns']}' existiert bereits im System."
            )

        printer = Printer.from_dict(printer_data)
        location.add_printer(printer)
        self._commit()

    def remove_printer_from_location(self, printer_dns: str, location_name: str):
        location = self.get_location_by_name(location_name)
        if not location:
            raise ItemNotFoundError(f"Standort '{location_name}' nicht gefunden.")

        try:
            location.remove_printer(printer_dns)
            self._commit()
        except ValueError:
            raise ItemNotFoundError(
                f"Drucker mit DNS '{printer_dns}' am Standort '{location_name}' nicht gefunden."
            )

    def update_printer(self, original_dns: str, new_data: Dict[str, Any]):
        result = self.get_printer_by_dns(original_dns)
        if not result:
            raise ItemNotFoundError(f"Drucker mit DNS '{original_dns}' nicht gefunden.")

        printer, location = result

        # Falls DNS geändert wurde, prüfen ob der neue schon existiert
        if original_dns != new_data["dns"] and self.get_printer_by_dns(new_data["dns"]):
            raise ValueError(
                f"Der neue DNS-Name '{new_data['dns']}' ist bereits vergeben."
            )

        printer.dns = new_data["dns"]
        printer.name = new_data["name"]
        printer.model = new_data["model"]
        printer.driver_name = new_data["driver_name"]
        printer.driver_inf_path = new_data["driver_inf_path"]
        self._commit()

    def create_backup(self, path: str = None):
        self._storage.create_manual_backup(path or self._storage.backup_filepath)

    def restore_from_backup(self, path: str = None):
        self._storage.restore_from_backup(path or self._storage.backup_filepath)
        self.load_data()  # Daten nach Wiederherstellung neu laden
