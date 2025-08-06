# threads/load_installed_printers_thread.py

from PySide6.QtCore import QThread, Signal
import win32print

class LoadInstalledPrintersThread(QThread):

    # Signal bei einem Fehler während der Installation (mit Fehlermeldung)
    printer_found = Signal(str)

    def __init__(self):
        super().__init__()


    def run(self):
        try:
            # PRINTER_ENUM_LOCAL | PRINTER_ENUM_CONNECTIONS выводит локальные и сетевые принтеры
            printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
            if not printers:
                return
            for printer in printers:
                self.printer_found.emit(printer[2])

        except Exception as e:
            raise