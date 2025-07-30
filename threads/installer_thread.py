# threads/installer_thread.py

import subprocess
import os
from PySide6.QtCore import QThread, Signal
from models.printer import Printer


class InstallerThread(QThread):
    """
    Führt die Installationsbefehle für einen Drucker in einem separaten Thread aus.
    Kommuniziert das Ergebnis über Signale.
    """

    # Signal für jeden erfolgreich abgeschlossenen Schritt
    step_finished = Signal()
    # Signal bei erfolgreichem Abschluss der gesamten Installation (mit Erfolgsmeldung)
    installation_finished = Signal(str)
    # Signal bei einem Fehler während der Installation (mit Fehlermeldung)
    installation_failed = Signal(str)

    def __init__(self, printer: Printer):
        super().__init__()
        self.__printer = printer
        self.__commands = self._build_commands()

    def _build_commands(self) -> list[str]:
        """Baut die Liste der auszuführenden Shell-Befehle."""
        port_name = f"IP_{self.__printer.dns}"
        return [
            (
                f'cscript "C:\\Windows\\System32\\Printing_Admin_Scripts\\de-DE\\prnport.vbs" '
                f"-a -r {port_name} -h {self.__printer.dns} -o raw -n 9100"
            ),
            (f'pnputil /add-driver "{os.path.join(os.getcwd(), self.__printer.driver_inf_path)}" /install'),
            (
                f'rundll32 printui.dll,PrintUIEntry /if /b "{self.__printer.name}" /r "{port_name}" '
                f'/f "{os.path.join(os.getcwd(), self.__printer.driver_inf_path)}" /m "{self.__printer.driver_name}" /z'
            ),
        ]

    def run(self) -> None:
        """Führt die Installationsschritte nacheinander aus."""
        try:
            for cmd in self.__commands:
                self.__run_command(cmd)
                self.step_finished.emit()

            success_msg = (
                f"Drucker '{self.__printer.name}' wurde erfolgreich installiert!"
            )
            self.installation_finished.emit(success_msg)

        except subprocess.CalledProcessError as e:
            error_msg = e.stderr or str(e)
            self.installation_failed.emit(error_msg)
        except Exception as e:
            self.installation_failed.emit(
                f"Ein unerwarteter Fehler ist aufgetreten: {e}"
            )

    def __run_command(self, command: str):
        """Führt einen einzelnen Shell-Befehl aus und wirft bei Fehlern eine Exception."""
        # capture_output=True, text=True sind wichtig für Fehlermeldungen

        subprocess.run(command, shell=True, capture_output=True, text=True)
        # Der `check=True` Parameter sorgt dafür, dass bei einem non-zero return code eine CalledProcessError ausgelöst wird.
