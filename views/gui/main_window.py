# views/gui/main_window.py

from PySide6.QtWidgets import QMainWindow, QMessageBox, QTreeWidgetItem
from PySide6.QtCore import QThread
from .ui.main_window_ui import Ui_MainWindow
from .create_printer import CreatePrinterDialog
from .create_location import CreateLocationDialog
from services.printer_service import PrinterService, LocationNotEmptyError, ItemNotFoundError
from models.printer import Printer
from threads.installer_thread import InstallerThread
from threads.availability_check_thread import AvailabilityCheckThread

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, service: PrinterService):
        super().__init__()
        self.setupUi(self)
        self.service = service
        self.current_printer: Printer | None = None
        self.current_item: QTreeWidgetItem | None = None

        self._worker_thread = None  # Generischer Thread für Hintergrundaufgaben

        self._connect_signals()
        self.load_storage_to_gui()

    def _connect_signals(self):
        self.createItemComboBox.textActivated.connect(self.on_create_item)
        self.printersTreeWidget.currentItemChanged.connect(self.on_item_changed)
        self.deleteItemButton.clicked.connect(self.on_delete_item)
        self.installPrinterButton.clicked.connect(self.on_install_printer)
        self.editPrinterButton.clicked.connect(self.on_edit_item)
        self.searchEdit.textChanged.connect(self.on_search)

    def load_storage_to_gui(self):
        self.printersTreeWidget.clear()
        locations = self.service.get_all_locations()
        for location in locations:
            location_item = QTreeWidgetItem([location.name])
            self.printersTreeWidget.addTopLevelItem(location_item)
            for printer in location.printers:
                printer_item = QTreeWidgetItem([printer.name])
                # Speichern des DNS-Namens als eindeutige ID im Item
                printer_item.setData(1, 0, printer.dns)
                location_item.addChild(printer_item)
        self.printersTreeWidget.expandAll()
        self.statusbar.showMessage("Daten erfolgreich geladen.", 3000)

    def on_item_changed(self, current: QTreeWidgetItem, previous: QTreeWidgetItem):
        self.installPrinterButton.setEnabled(False)
        self.editPrinterButton.setEnabled(False)
        self.current_item = current
        self.current_printer = None
        
        if not current or current.parent() is None: # Es ist ein Standort oder nichts
            self.clear_printer_details()
            return

        # Es ist ein Drucker
        self.editPrinterButton.setEnabled(True)
        printer_dns = current.data(1, 0)
        result = self.service.get_printer_by_dns(printer_dns)
        if not result:
            self.clear_printer_details()
            return

        printer, location = result
        self.current_printer = printer
        self.update_printer_details(printer, location.name)
        self.check_printer_availability(printer)

    def update_printer_details(self, printer: Printer, location_name: str):
        self.locationLabel.setText(location_name)
        self.printerNameLabel.setText(printer.name)
        self.printerModelLabel.setText(printer.model)
        self.DNSNameLabel.setText(printer.dns)
        self.driverNameLabel.setText(printer.driver_name)
        self.driverPathLabel.setText(printer.driver_inf_path)
        self.availableLabel.setStyleSheet("color: white;")
        self.availableLabel.setText("PRÜFUNG LÄUFT...")

    def clear_printer_details(self):
        self.locationLabel.setText("N/A")
        self.printerNameLabel.setText("N/A")
        self.printerModelLabel.setText("N/A")
        self.DNSNameLabel.setText("N/A")
        self.driverNameLabel.setText("N/A")
        self.driverPathLabel.setText("N/A")
        self.availableLabel.setText("N/A")
        self.availableLabel.setStyleSheet("")

    def check_printer_availability(self, printer: Printer):
        if self._worker_thread and self._worker_thread.isRunning():
            self._worker_thread.terminate()
        
        self._worker_thread = AvailabilityCheckThread(printer)
        self._worker_thread.availability_check_finished.connect(self.on_availability_checked)
        self._worker_thread.start()

    def on_availability_checked(self, is_available: bool):
        color = "lightgreen" if is_available else "salmon"
        self.availableLabel.setText("JA" if is_available else "NEIN")
        self.availableLabel.setStyleSheet(f"color: {color}; font-weight: bold;")
        if self.current_printer:
            self.installPrinterButton.setEnabled(is_available)

    def on_create_item(self, item_type: str):
        if item_type == "Drucker":
            self.create_printer()
        elif item_type == "Standort":
            self.create_location()
        self.createItemComboBox.setCurrentIndex(0) # Zurücksetzen

    def create_printer(self):
        dialog = CreatePrinterDialog(self.service)
        if dialog.exec():
            try:
                printer_data, location_name = dialog.get_result()
                self.service.add_printer_to_location(printer_data, location_name)
                self.load_storage_to_gui()
                self.statusbar.showMessage("Drucker erfolgreich erstellt!", 3000)
            except (ValueError, ItemNotFoundError) as e:
                QMessageBox.critical(self, "Fehler", str(e))

    def create_location(self):
        dialog = CreateLocationDialog(self.service)
        if dialog.exec():
            try:
                location_name = dialog.get_result()
                self.service.add_location(location_name)
                self.load_storage_to_gui()
                self.statusbar.showMessage("Standort erfolgreich erstellt!", 3000)
            except ValueError as e:
                QMessageBox.critical(self, "Fehler", str(e))

    def on_edit_item(self):
        if not self.current_printer:
            return
            
        dialog = CreatePrinterDialog(self.service, printer=self.current_printer, edit_mode=True)
        if dialog.exec():
            try:
                original_dns, new_data = dialog.get_result()
                self.service.update_printer(original_dns, new_data)
                self.load_storage_to_gui()
                self.statusbar.showMessage("Drucker erfolgreich aktualisiert!", 3000)
            except (ValueError, ItemNotFoundError) as e:
                QMessageBox.critical(self, "Fehler", str(e))
    
    def on_delete_item(self):
        if not self.current_item:
            return

        item_name = self.current_item.text(0)
        is_location = self.current_item.parent() is None

        reply = QMessageBox.warning(self, "Löschen bestätigen", 
                                    f"Möchten Sie '{item_name}' wirklich endgültig löschen?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

        if reply == QMessageBox.StandardButton.Yes:
            try:
                if is_location:
                    self.service.remove_location(item_name)
                else:
                    location_name = self.current_item.parent().text(0)
                    printer_dns = self.current_item.data(1, 0)
                    self.service.remove_printer_from_location(printer_dns, location_name)
                
                self.load_storage_to_gui()
                self.clear_printer_details()
                self.statusbar.showMessage("Eintrag erfolgreich gelöscht!", 3000)

            except (LocationNotEmptyError, ItemNotFoundError) as e:
                QMessageBox.critical(self, "Fehler", str(e))

    def on_install_printer(self):
        if not self.current_printer or not self.current_printer.is_available():
            QMessageBox.warning(self, "Aktion nicht möglich", "Kein installierbarer Drucker ausgewählt oder Drucker nicht erreichbar.")
            return

        self.progressBar.setValue(0)
        self.progressBar.setMaximum(3)
        self.progressBar.setFormat("[Schritt 0/3] Installation wird vorbereitet...")
        
        self.installer_thread = InstallerThread(self.current_printer, is_gui=True)
        self.installer_thread.step_finished.connect(self.on_installation_step)
        self.installer_thread.installation_finished.connect(self.on_installation_finished)
        self.installer_thread.installation_failed.connect(self.on_installation_failed)
        self.installer_thread.start()

    def on_installation_step(self):
        value = self.progressBar.value() + 1
        self.progressBar.setValue(value)
        self.progressBar.setFormat(f"[Schritt {value}/3] Installation läuft...")

    def on_installation_finished(self, message):
        self.progressBar.setFormat(message)
        QMessageBox.information(self, "Erfolg", message)

    def on_installation_failed(self, error_message):
        self.progressBar.setFormat(f"Fehler: {error_message}")
        QMessageBox.critical(self, "Installationsfehler", error_message)

    def on_search(self, text: str):
        # Einfache Suche, die alle Items durchgeht
        # Für große Datenmengen sollte dies optimiert werden
        term = text.lower()
        root = self.printersTreeWidget.invisibleRootItem()
        for i in range(root.childCount()):
            location_item = root.child(i)
            location_visible = term in location_item.text(0).lower()
            
            has_visible_child = False
            for j in range(location_item.childCount()):
                printer_item = location_item.child(j)
                printer_dns = printer_item.data(1, 0)
                # Suchen nach Name, Standort oder DNS
                printer_visible = term in printer_item.text(0).lower() or term in printer_dns.lower()
                printer_item.setHidden(not printer_visible)
                if printer_visible:
                    has_visible_child = True
            
            location_item.setHidden(not (location_visible or has_visible_child))

    def closeEvent(self, event):
        # Sicherstellen, dass alle Threads beendet werden
        if self._worker_thread and self._worker_thread.isRunning():
            self._worker_thread.terminate()
        super().closeEvent(event)