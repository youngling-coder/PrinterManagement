# main_gui.py

import sys
from PySide6.QtWidgets import QApplication
from data.storage import Storage
from services.printer_service import PrinterService
from views.gui.main_window import MainWindow

def main():
    """Initialisiert und startet die grafische Benutzeroberfläche."""
    app = QApplication(sys.argv)

    # 1. Datenzugriffsschicht initialisieren
    storage = Storage("printers.json")

    # 2. Service-Schicht mit dem Storage initialisieren
    try:
        printer_service = PrinterService(storage)
    except FileNotFoundError as e:
        # Frühes Abfangen, falls die JSON-Datei fehlt und kein Backup existiert
        QApplication.instance().exit()
        print(f"Fehler beim Start: {e}")
        # Hier könnte man einen Dialog anzeigen, um eine Datei auszuwählen
        return

    # 3. View mit dem Service initialisieren
    gui = MainWindow(printer_service)
    gui.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()