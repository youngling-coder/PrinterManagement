# threads/load_installed_printers_thread.py

from PySide6.QtCore import QThread, Signal
from models.printer import Printer
import win32print
import wmi

class LoadInstalledPrintersThread(QThread):

    # Signal bei einem Fehler während der Installation (mit Fehlermeldung)
    printer_found = Signal(Printer, int)
    printer_collection_found = Signal(int)

    def __init__(self):
        super().__init__()


    def run(self):
        try:
            printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
            
            if not printers:
                return
            
            self.printer_collection_found.emit(len(printers))
            
            for idx, printer in enumerate(printers):
                
                printer_name = printer[2]
                wmi_connection = wmi.WMI()
                printers = wmi_connection.Win32_Printer(Name=printer_name)
        
                printer = Printer.from_dict(
                    {
                        "dns": "N/A" if not printers else printers[0].PortName[3:],
                        "name": printer_name if not printers else printers[0].Name,
                        "model": "N/A",
                        "driver_name": "N/A" if not printers else printers[0].DriverName,
                        "driver_inf_path": "N/A"
                    }
                )

                self.printer_found.emit(printer, idx)

        except Exception as e:
            raise