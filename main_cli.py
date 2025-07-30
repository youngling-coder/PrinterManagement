# main_cli.py

import os
from data.storage import Storage
from services.printer_service import (
    PrinterService,
    LocationNotEmptyError,
    ItemNotFoundError,
)
from views.cli import cli_input, cli_output
from threads.installer_thread import InstallerThread


class CliApplication:
    """Eine Klasse, um den Zustand der CLI-Anwendung zu kapseln."""

    def __init__(self, service: PrinterService):
        self.service = service
        self.actions = {
            1: self.show_overview,
            2: self.add_printer,
            3: self.remove_printer,
            4: self.install_printer,
            5: self.add_location,
            6: self.remove_location,
            7: self.restore_backup,
            8: self.create_backup,
        }

    def run(self):
        """Startet die interaktive Endlosschleife."""
        os.system("cls || clear")  # Funktioniert auf Windows und Unix-Systemen
        while True:
            try:
                cli_output.print_menu()
                action_id = cli_input.get_current_action(len(self.actions))
                action_func = self.actions.get(action_id)
                if action_func:
                    action_func()
                else:
                    cli_output.print_error("Ungültige Aktion.")
            except (ItemNotFoundError, LocationNotEmptyError) as e:
                cli_output.print_error(str(e))
            except KeyboardInterrupt:
                print("\nProgramm wird beendet.")
                break
            print()  # Leerzeile für bessere Lesbarkeit

    def show_overview(self):
        locations = self.service.get_all_locations()
        location_idx = cli_input.get_location_index_input(locations, optional=True)

        if location_idx is None:
            cli_output.print_full_overview(locations)
        else:
            location = locations[location_idx]
            cli_output.print_location_overview(location)

    def add_printer(self):
        locations = self.service.get_all_locations()
        if not locations:
            cli_output.print_error("Bitte erstellen Sie zuerst einen Standort.")
            return

        printer_data, location_name = cli_input.input_printer_data(locations)
        self.service.add_printer_to_location(printer_data, location_name)
        cli_output.print_success("Drucker wurde erfolgreich hinzugefügt.")

    def remove_printer(self):
        printer, location = cli_input.select_printer_data(
            self.service.get_all_locations()
        )
        if cli_input.get_yn_confirmation(
            f"Drucker '{printer.name}' wirklich entfernen?"
        ):
            self.service.remove_printer_from_location(printer.dns, location.name)
            cli_output.print_success("Drucker wurde erfolgreich entfernt.")

    def install_printer(self):
        printer, _ = cli_input.select_printer_data(self.service.get_all_locations())

        if not printer.is_available():
            cli_output.print_error("Drucker ist nicht erreichbar!")
            return

        if cli_input.get_yn_confirmation(
            f"Installation für '{printer.name}' fortsetzen?"
        ):
            installer = InstallerThread(printer)

            # Da die CLI blockierend ist, können wir die Signale nicht einfach nutzen.
            # Wir führen den Thread aus und warten, bis er fertig ist.
            # Für eine Fortschrittsanzeige müsste man komplexere Logik verwenden.
            installer.run()  # In der CLI rufen wir run() direkt auf.
            cli_output.print_success(
                f"Drucker '{printer.name}' wurde erfolgreich installiert!"
            )

    def add_location(self):
        name = cli_input.get_generic_input(
            "Name des neuen Standorts eingeben: ", empty=False
        )
        if cli_input.get_yn_confirmation(f"Standort '{name}' wirklich erstellen?"):
            self.service.add_location(name)
            cli_output.print_success("Standort wurde erfolgreich erstellt.")

    def remove_location(self):
        locations = self.service.get_all_locations()
        idx = cli_input.get_location_index_input(locations)
        location_name = locations[idx].name
        if cli_input.get_yn_confirmation(
            f"Standort '{location_name}' wirklich entfernen?"
        ):
            self.service.remove_location(location_name)
            cli_output.print_success("Standort wurde erfolgreich entfernt.")

    def restore_backup(self):
        path = cli_input.get_generic_input(
            "[Optional] Pfad zur Backup-Datei eingeben: "
        )
        if cli_input.get_yn_confirmation(
            "Aktuelle Daten werden überschrieben. Fortfahren?"
        ):
            self.service.restore_from_backup(path if path else None)
            cli_output.print_success("Daten erfolgreich aus Backup wiederhergestellt.")

    def create_backup(self):
        path = cli_input.get_generic_input("[Optional] Pfad für das Backup eingeben: ")
        self.service.create_backup(path if path else None)
        cli_output.print_success("Backup erfolgreich erstellt.")


def main():
    """Initialisiert und startet die Kommandozeilenanwendung."""
    try:
        storage = Storage("printers.json")
        printer_service = PrinterService(storage)
        app = CliApplication(printer_service)
        app.run()
    except Exception as e:
        cli_output.print_error(f"Ein kritischer Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    main()
