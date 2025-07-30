# views/gui/create_location.py

from PySide6.QtWidgets import QDialog, QMessageBox
from .ui.create_location_ui import Ui_CreateLocationDialog
from services.printer_service import PrinterService


class CreateLocationDialog(QDialog, Ui_CreateLocationDialog):
    def __init__(self, service: PrinterService):
        super().__init__()
        self.setupUi(self)
        self.service = service

        self.createButton.clicked.connect(self.on_accept)
        self.cancelButton.clicked.connect(self.reject)

    def on_accept(self):
        location_name = self.locationNameEdit.text().strip()
        if not location_name:
            QMessageBox.warning(
                self, "Fehlende Eingabe", "Der Standortname darf nicht leer sein."
            )
            return

        # Optionale, aber benutzerfreundliche Prüfung auf Duplikate direkt in der UI
        if self.service.get_location_by_name(location_name):
            QMessageBox.warning(
                self,
                "Konflikt",
                f"Ein Standort mit dem Namen '{location_name}' existiert bereits.",
            )
            return

        self.accept()

    def get_result(self) -> str:
        """Gibt den eingegebenen Standortnamen zurück."""
        return self.locationNameEdit.text().strip()
