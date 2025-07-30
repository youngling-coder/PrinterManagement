# threads/availability_check_thread.py

from PySide6.QtCore import QThread, Signal
from models.printer import Printer


class AvailabilityCheckThread(QThread):
    """Prüft die Verfügbarkeit eines Druckers in einem separaten Thread."""

    availability_check_finished = Signal(bool)

    def __init__(self, printer: Printer):
        super().__init__()
        self.__printer = printer

    def run(self) -> None:
        is_printer_available = self.__printer.is_available()
        self.availability_check_finished.emit(is_printer_available)
