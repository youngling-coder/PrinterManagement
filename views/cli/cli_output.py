# views/cli/cli_output.py

from colorama import Style, Fore, init
from prettytable import PrettyTable
from models.location import Location
from typing import List

# Initialisiert colorama für Windows
init(autoreset=True)

ACTIONS = [
    "Druckerübersicht anzeigen",
    "Neuen Drucker erstellen",
    "Einen Drucker entfernen",
    "Einen Drucker installieren",
    "Einen neuen Standort erstellen",
    "Einen Standort entfernen",
    "Aus Backup wiederherstellen",
    "Manuelles Backup erstellen",
]


def print_error(msg: str):
    """Gibt eine formatierte Fehlermeldung aus."""
    print(f"{Style.BRIGHT}{Fore.RED}❌ Fehler: {msg}")


def print_success(msg: str):
    """Gibt eine formatierte Erfolgsmeldung aus."""
    print(f"{Style.BRIGHT}{Fore.GREEN}✅ {msg}")


def print_warning(msg: str):
    """Gibt eine formatierte Warnung aus."""
    print(f"{Style.BRIGHT}{Fore.YELLOW}⚠️ {msg}")


def print_menu():
    """Gibt das Hauptmenü der Aktionen aus."""
    print(
        f'Geben Sie {Style.BRIGHT}"exit"{Style.RESET_ALL} oder drücken Sie Strg+C, um das Programm zu beenden.\n'
    )
    for idx, action in enumerate(ACTIONS):
        print(f"{Style.BRIGHT}{idx + 1}.{Style.RESET_ALL} {action}")
    print()


def print_location_overview(location: Location):
    """Zeigt eine tabellarische Übersicht der Drucker eines Standorts."""
    print(f"\n{Style.BRIGHT}Standort: {location.name}{Style.RESET_ALL}")

    if not location.printers:
        print(Fore.LIGHTBLACK_EX + "  (Keine Drucker an diesem Standort vorhanden)")
        return

    table = PrettyTable()
    table.field_names = ["#", "Name", "DNS-Name", "Modell", "Treiber", "Verfügbar"]
    table.align = "l"

    for i, printer in enumerate(location.printers):
        # Verfügbarkeitsprüfung (kann bei vielen Druckern dauern)
        status = printer.is_available()
        status_icon = (
            f"{Fore.GREEN}Ja{Style.RESET_ALL}"
            if status
            else f"{Fore.RED}Nein{Style.RESET_ALL}"
        )
        table.add_row(
            [
                i + 1,
                printer.name,
                printer.dns,
                printer.model,
                printer.driver_name,
                status_icon,
            ]
        )
    print(table)


def print_full_overview(locations: List[Location]):
    """Zeigt eine Übersicht über alle Standorte und deren Drucker."""
    if not locations:
        print_warning("Keine Standorte vorhanden.")
        return

    for location in locations:
        print_location_overview(location)


def format_locations_for_selection(locations: List[Location]) -> str:
    """Formatiert eine nummerierte Liste von Standorten für die Auswahl."""
    if not locations:
        return "Keine Standorte zur Auswahl."
    return "\n".join(
        [
            f"{Style.BRIGHT}{i + 1}.{Style.RESET_ALL} {loc.name}"
            for i, loc in enumerate(locations)
        ]
    )
