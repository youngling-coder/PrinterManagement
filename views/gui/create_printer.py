# views/gui/create_printer.py

from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from .ui.create_printer_ui import Ui_CreatePrinterDialog
from services.printer_service import PrinterService
from models.printer import Printer
from typing import Optional, Tuple, Dict, Any


class CreatePrinterDialog(QDialog, Ui_CreatePrinterDialog):
    def __init__(
        self,
        service: PrinterService,
        printer: Optional[Printer] = None,
        edit_mode: bool = False,
    ):
        super().__init__()
        self.setupUi(self)

        self.service = service
        self.printer = printer
        self.edit_mode = edit_mode

        self._populate_locations()
        self._configure_ui()

        self.driverPathEdit.mousePressEvent = self._select_driver_file
        self.createButton.clicked.connect(self._on_accept)
        self.cancelButton.clicked.connect(self.reject)

    def _configure_ui(self):
        if self.edit_mode:
            self.setWindowTitle("Drucker bearbeiten")
            self.createButton.setText("Übernehmen")
            if self.printer:
                self._load_printer_data()
        else:
            self.setWindowTitle("Neuen Drucker erstellen")

    def _populate_locations(self):
        locations = self.service.get_all_locations()
        for location in locations:
            self.locationComboBox.addItem(location.name)

        if not locations and not self.edit_mode:
            QMessageBox.warning(
                self,
                "Keine Standorte",
                "Bitte erstellen Sie zuerst einen Standort, bevor Sie einen Drucker hinzufügen.",
            )
            self.createButton.setEnabled(False)

    def _load_printer_data(self):
        self.DNSNameEdit.setText(self.printer.dns)
        self.printerNameEdit.setText(self.printer.name)
        self.printerModelEdit.setText(self.printer.model)
        self.driverNameEdit.setText(self.printer.driver_name)
        self.driverPathEdit.setText(self.printer.driver_inf_path)

        # Den Standort des Druckers in der ComboBox auswählen
        _, location = self.service.get_printer_by_dns(self.printer.dns)
        if location:
            self.locationComboBox.setCurrentText(location.name)
            self.locationComboBox.setEnabled(
                False
            )  # Standort kann nicht geändert werden

    def _on_accept(self):
        # Einfache Validierung, ob alle Felder ausgefüllt sind
        fields = [
            self.DNSNameEdit,
            self.printerNameEdit,
            self.printerModelEdit,
            self.driverNameEdit,
            self.driverPathEdit,
        ]
        if any(not field.text().strip() for field in fields):
            QMessageBox.warning(
                self, "Fehlende Eingabe", "Alle Felder müssen ausgefüllt werden."
            )
            return
        self.accept()

    def get_result(self) -> Tuple[str, Dict[str, Any]] | Tuple[Dict[str, Any], str]:
        """Gibt die gesammelten Daten zurück."""
        data = {
            "dns": self.DNSNameEdit.text().strip(),
            "name": self.printerNameEdit.text().strip(),
            "model": self.printerModelEdit.text().strip(),
            "driver_name": self.driverNameEdit.text().strip(),
            "driver_inf_path": self.driverPathEdit.text().strip(),
        }

        if self.edit_mode:
            # Gibt die Original-DNS und die neuen Daten zurück
            return self.printer.dns, data
        else:
            # Gibt die neuen Daten und den ausgewählten Standortnamen zurück
            location_name = self.locationComboBox.currentText()
            return data, location_name

    def _select_driver_file(self, event: QMouseEvent):
        # Zeigt einen Dateidialog, um eine .inf Datei auszuwählen
        if event.button() == Qt.MouseButton.LeftButton:
            path, _ = QFileDialog.getOpenFileName(
                self, "Treiberdatei auswählen", "", "Treiber-Informationen (*.inf)"
            )
            if path:
                self.driverPathEdit.setText(path)
