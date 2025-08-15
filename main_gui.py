# main_gui.py

import sys
from PySide6.QtWidgets import QApplication
from crud.database import create_db_from_schema
from views.gui.main_window import MainWindow


def main():
    """Initialisiert und startet die grafische Benutzeroberfläche."""
    app = QApplication(sys.argv)

    # 1. Datenzugriffsschicht initialisieren
    # storage = Storage("printers.json")

    # 2. View mit dem Service initialisieren
    gui = MainWindow()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    create_db_from_schema()
    main()

input()
