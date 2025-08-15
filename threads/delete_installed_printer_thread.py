# threads/delete_installed_printer_thread.py

from PySide6.QtCore import QThread, Signal
import wmi


class UninstallPrinterThread(QThread):

    printer_uninstalled = Signal(str)
    printer_uninstall_failed = Signal(str)

    def __init__(self, printer_name: str):
        super().__init__()

        self.printer_name = printer_name

    def run(self):
        try:
            wmi_connection = wmi.WMI()

            printers = wmi_connection.Win32_Printer(Name=self.printer_name)

            for printer in printers:
                printer.Delete_()
                self.printer_uninstalled.emit(self.printer_name)
                return

        except wmi.x_wmi as e:
            error_info = e.com_error
            if error_info.hresult == -2147217405:
                self.printer_uninstall_failed.emit(f"Zugriff verweigert!")
            else:
                self.printer_uninstall_failed.emit(
                    f"Ein WMI Fehler ist aufgetreten: : {e}"
                )

        except Exception as e:
            self.printer_uninstall_failed.emit(
                f"Ein unerwarteter Fehler ist aufgetreten: {e}"
            )
