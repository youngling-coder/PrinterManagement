# views/gui/main_window.py

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTreeWidgetItem, QListWidgetItem

from .ui.main_window_ui import Ui_MainWindow
from .create_printer import CreatePrinterDialog
from .create_location import CreateLocationDialog

from models.printer import Printer
from models.location import Location


from threads.installer_thread import InstallerThread
from threads.availability_check_thread import AvailabilityCheckThread
from threads.load_installed_printers_thread import LoadInstalledPrintersThread
from threads.delete_installed_printer_thread import UninstallPrinterThread

from crud.locations import (
    get_locations,
    get_location_by_name,
    get_location_by_id,
    create_location,
    delete_location,
)
from crud.printers import (
    get_printer_by_dns,
    get_printers_by_location_id,
    create_printer,
    update_printer,
    delete_printer,
)
import webbrowser


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_printer: Printer | None = None
        self.current_location: Location | None = None
        self.current_item: QTreeWidgetItem | None = None
        self.installed_printer_collection_count: int = 0

        self._check_availability_thread = None
        self._load_installed_printers_thread = None
        self._uninstall_printer_thread = None
        self._installer_thread = None

        self._connect_signals()
        self.load_storage_to_gui()
        self.on_installed_printers_refresh()

    def _connect_signals(self):
        self.createItemComboBox.textActivated.connect(self.on_create_item)
        self.printersTreeWidget.currentItemChanged.connect(self.on_item_changed)
        self.installedPrintersListWidget.currentItemChanged.connect(
            self.on_installed_printer_item_changed
        )
        self.deleteItemButton.clicked.connect(self.on_delete_item)
        self.installPrinterButton.clicked.connect(self.on_printer_install)
        self.editPrinterButton.clicked.connect(self.on_edit_item)
        self.searchEdit.textChanged.connect(self.on_search)
        self.openDocumentationAction.triggered.connect(self.on_documentation_load)
        self.installedPrintersRefreshButton.clicked.connect(
            self.on_installed_printers_refresh
        )
        self.uninstallPrinterButton.clicked.connect(self.on_printer_uninstall)

    def on_printer_uninstalled(self, printer_name: str):
        QMessageBox.information(
            self,
            "Erfolg!",
            f"Drucker mit dem Namen '{printer_name}' wurde erfolgreich deinstalliert!",
        )
        self.on_installed_printers_refresh()
        self.uninstallPrinterButton.setEnabled(True)

    def on_printer_uninstall_failed(self, error):
        QMessageBox.critical(self, "Fehler!", error)
        self.uninstallPrinterButton.setEnabled(True)

    def on_printer_uninstall(self):

        if self.installedPrintersListWidget.currentItem():

            self.uninstallPrinterButton.setEnabled(False)
            printer_name = self.installedPrintersListWidget.currentItem().text()

            if self._uninstall_printer_thread:
                self._uninstall_printer_thread.terminate()
                self._uninstall_printer_thread.quit()
                self._uninstall_printer_thread.wait()

            self._uninstall_printer_thread = UninstallPrinterThread(printer_name)
            self._uninstall_printer_thread.printer_uninstalled.connect(
                self.on_printer_uninstalled
            )
            self._uninstall_printer_thread.printer_uninstall_failed.connect(
                self.on_printer_uninstall_failed
            )
            self._uninstall_printer_thread.start()

    def on_printer_found(self, printer: Printer, index: int):
        self.progressBar.setValue(index + 1)
        self.progressBar.setFormat(
            f"[{index+1}/{self.installed_printer_collection_count}] Überprüfe installierte Drucker..."
        )
        new_printer_widget_item = QListWidgetItem(printer.name)
        self.installedPrintersListWidget.addItem(new_printer_widget_item)
        new_printer_widget_item.setData(Qt.UserRole, printer)

        if index + 1 == self.installed_printer_collection_count:
            self.statusbar.showMessage("Installierte Drucker wurden überpruft!", 3000)
            self.progressBar.setFormat("")
            self.installedPrintersRefreshButton.setEnabled(True)

    def on_printer_collection_found(self, count: int):
        self.progressBar.setValue(self.progressBar.value())
        self.installed_printer_collection_count = count
        self.progressBar.setMaximum(count)

    def on_installed_printers_refresh(self):

        if self._load_installed_printers_thread:
            if self._load_installed_printers_thread.isRunning():
                return

        self.installedPrintersRefreshButton.setEnabled(False)
        self.progressBar.setValue(0)
        self.installedPrintersListWidget.clear()

        self._load_installed_printers_thread = LoadInstalledPrintersThread()
        self._load_installed_printers_thread.printer_found.connect(
            self.on_printer_found
        )
        self._load_installed_printers_thread.printer_collection_found.connect(
            self.on_printer_collection_found
        )
        self._load_installed_printers_thread.start()

    def on_documentation_load(self):
        webbrowser.open("https://docs.nachtblau.tv/node/36630/")

    def load_storage_to_gui(self):
        self.printersTreeWidget.clear()
        locations = get_locations()

        if locations:
            for location in locations:
                location_item = QTreeWidgetItem([location["name"]])
                self.printersTreeWidget.addTopLevelItem(location_item)

                printers = get_printers_by_location_id(location["id"])
                for printer in printers:
                    printer_item = QTreeWidgetItem([printer["name"]])
                    printer_item.setData(0, Qt.UserRole, printer["dns"])
                    location_item.addChild(printer_item)
        self.printersTreeWidget.expandAll()
        self.statusbar.showMessage("Daten erfolgreich geladen.", 3000)

    def on_item_changed(self, current: QTreeWidgetItem):
        self.current_item = current
        self.current_printer = None
        self.current_location = None

        item_name = self.printersTreeWidget.currentItem().text(0)

        if not current or current.parent() is None:
            self.current_location = Location.from_dict(get_location_by_name(item_name))
            self.installPrinterButton.setEnabled(False)
            self.editPrinterButton.setEnabled(False)
            if self._check_availability_thread:
                self._check_availability_thread.terminate()
                self._check_availability_thread.quit()
                self._check_availability_thread.wait()
            self.clear_printer_details()
            return

        # Es ist ein Drucker
        result = get_printer_by_dns(
            self.printersTreeWidget.currentItem().data(0, Qt.UserRole)
        )
        if not result:
            self.clear_printer_details()
            return

        printer = Printer.from_dict(result)
        location = Location.from_dict(get_location_by_id(printer.location_id))
        self.current_printer = printer
        self.current_location = location
        self.update_printer_details(printer, location.name)
        self.check_printer_availability(printer)

        self.editPrinterButton.setEnabled(True)
        self.installPrinterButton.setEnabled(True)

    def on_installed_printer_item_changed(self, current: QListWidgetItem):
        if not current:
            self.clear_printer_details()
            return

        printer = current.data(Qt.UserRole)
        self.check_printer_availability(printer)
        self.update_printer_details(printer, location_name="N/A")

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
        self.availableLabel.setStyleSheet("N/A")

    def check_printer_availability(self, printer: Printer):
        if self._check_availability_thread:
            self._check_availability_thread.terminate()
            self._check_availability_thread.quit()
            self._check_availability_thread.wait()

        self._check_availability_thread = AvailabilityCheckThread(printer)
        self._check_availability_thread.availability_check_finished.connect(
            self.on_availability_checked
        )
        self._check_availability_thread.start()

    def on_availability_checked(self, is_available: bool):
        color = "lightgreen" if is_available else "salmon"
        self.availableLabel.setText("JA" if is_available else "NEIN")
        self.availableLabel.setStyleSheet(f"color: {color}; font-weight: bold;")
        if self.current_printer:
            if self._installer_thread:
                self.installPrinterButton.setEnabled(
                    is_available and self._installer_thread.isFinished()
                )
            else:
                self.installPrinterButton.setEnabled(is_available)

    def on_create_item(self, item_type: str):
        if item_type == "Drucker":
            if get_locations():
                self.create_printer()
            else:
                QMessageBox.critical(self, "Fehler", "Keine Standorte vorhanden!")
                return

        elif item_type == "Standort":
            self.create_location()
        self.createItemComboBox.setCurrentIndex(0)  # Zurücksetzen

    def create_printer(self):
        dialog = CreatePrinterDialog(self.current_location)
        if dialog.exec():
            try:
                printer_data = dialog.get_result()

                create_printer(printer_data)

                self.load_storage_to_gui()
                self.statusbar.showMessage("Drucker erfolgreich erstellt!", 3000)

            except Exception as e:
                QMessageBox.critical(self, "Fehler", str(e))

    def create_location(self):
        dialog = CreateLocationDialog()
        if dialog.exec():
            try:
                location_name = dialog.get_result()
                create_location(location_name)
                self.load_storage_to_gui()
                self.statusbar.showMessage("Standort erfolgreich erstellt!", 3000)
            except ValueError as e:
                QMessageBox.critical(self, "Fehler", str(e))

    def on_edit_item(self):
        if not self.current_printer:
            return

        dialog = CreatePrinterDialog(printer=self.current_printer, edit_mode=True)
        if dialog.exec():
            try:
                new_data = dialog.get_result()
                update_printer(self.current_printer.id, new_data)
                self.load_storage_to_gui()
                self.statusbar.showMessage("Drucker erfolgreich aktualisiert!", 3000)
            except Exception as e:
                QMessageBox.critical(self, "Fehler", str(e))

    def on_delete_item(self):
        if not self.current_item:
            return

        item_name = self.current_item.text(0)
        is_location = self.current_item.parent() is None

        reply = QMessageBox.warning(
            self,
            "Löschen bestätigen",
            f"Möchten Sie '{item_name}' wirklich endgültig löschen?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                if is_location:
                    if self.current_item.childCount() < 1:
                        delete_location(get_location_by_name(item_name)["id"])

                    else:
                        QMessageBox.critical(
                            self,
                            "Fehler",
                            f"Standort '{item_name}' enthält noch Drucker und kann nicht gelöscht werden.",
                        )
                        return

                else:
                    printer_index = self.current_printer.id
                    delete_printer(printer_index)

                self.load_storage_to_gui()
                self.clear_printer_details()
                self.statusbar.showMessage("Eintrag erfolgreich gelöscht!", 3000)

            except Exception as e:
                QMessageBox.critical(self, "Fehler", str(e))

    def on_printer_install(self):
        if not self.current_printer or not self.current_printer.is_available():
            QMessageBox.warning(
                self,
                "Aktion nicht möglich",
                "Kein installierbarer Drucker ausgewählt oder Drucker nicht erreichbar.",
            )
            return

        self.installPrinterButton.setEnabled(False)
        self.editPrinterButton.setEnabled(False)
        self.deleteItemButton.setEnabled(False)
        self.progressBar.setValue(0)
        self.progressBar.setMaximum(3)
        self.progressBar.setFormat("[Schritt 0/3] Installation wird vorbereitet...")

        if self._load_installed_printers_thread:
            self._load_installed_printers_thread.terminate()
            self._load_installed_printers_thread.quit()
            self._load_installed_printers_thread.wait()

        self._installer_thread = InstallerThread(
            self.current_printer, self.current_location
        )
        self._installer_thread.step_finished.connect(self.on_installation_step)
        self._installer_thread.installation_finished.connect(
            self.on_installation_finished
        )
        self._installer_thread.installation_failed.connect(self.on_installation_failed)
        self._installer_thread.start()

    def on_installation_step(self):
        value = self.progressBar.value() + 1
        self.progressBar.setValue(value)
        self.progressBar.setFormat(f"[Schritt {value}/3] Installation läuft...")

    def on_installation_finished(self, message):
        self.progressBar.setFormat(message)
        QMessageBox.information(self, "Erfolg", message)
        self.installPrinterButton.setEnabled(True)
        self.editPrinterButton.setEnabled(True)
        self.deleteItemButton.setEnabled(True)

    def on_installation_failed(self, error_message):
        self.progressBar.setFormat(f"Fehler: {error_message}")
        QMessageBox.critical(self, "Installationsfehler", error_message)
        self.installPrinterButton.setEnabled(True)
        self.editPrinterButton.setEnabled(True)
        self.deleteItemButton.setEnabled(True)

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

                # Suchen nach Name, Standort oder DNS
                printer_visible = term in printer_item.text(
                    0
                ).lower() or term in printer_item.data(0, Qt.UserRole)
                printer_item.setHidden(not printer_visible)
                if printer_visible:
                    has_visible_child = True

            location_item.setHidden(not (location_visible or has_visible_child))
