# views/cli/cli_input.py

import sys
from typing import List, Optional, Tuple, Dict, Any
from colorama import Style
from models.location import Location
from models.printer import Printer
from . import cli_output


def get_generic_input(prompt: str, empty: bool = True) -> str:
    """Fragt eine generische Benutzereingabe ab."""
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            print("Programm wird beendet.")
            sys.exit(0)
        if not empty and not value:
            cli_output.print_error("Eingabe darf nicht leer sein.")
            continue
        return value


def get_yn_confirmation(prompt: str) -> bool:
    """Fragt eine Ja/Nein-Bestätigung ab."""
    full_prompt = f"{Style.BRIGHT}{prompt} [Y/n]: {Style.RESET_ALL}"
    confirmation = get_generic_input(full_prompt)
    return confirmation.lower().startswith("y") or confirmation == ""


def get_integer_input(
    prompt: str, min_val: int, max_val: int, optional: bool = False
) -> Optional[int]:
    """Fragt eine Ganzzahl in einem bestimmten Bereich ab."""
    while True:
        value_str = get_generic_input(prompt, empty=optional)
        if optional and not value_str:
            return None
        try:
            value_int = int(value_str)
            if min_val <= value_int <= max_val:
                return value_int
            else:
                cli_output.print_error(
                    f"Bitte geben Sie eine Zahl zwischen {min_val} und {max_val} ein."
                )
        except ValueError:
            cli_output.print_error(
                "Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein."
            )


def get_current_action(max_action: int) -> int:
    """Fragt die gewünschte Aktion vom Benutzer ab."""
    return get_integer_input("Wählen Sie die gewünschte Aktion: ", 1, max_action)


def get_location_index_input(
    locations: List[Location], optional: bool = False
) -> Optional[int]:
    """Zeigt alle Standorte an und fragt den Index ab."""
    if not locations:
        cli_output.print_warning("Keine Standorte gefunden.")
        return None

    print("\nVerfügbare Standorte:")
    print(cli_output.format_locations_for_selection(locations))

    prompt = "Nummer des Standorts eingeben"
    if optional:
        prompt += " (oder Enter zum Überspringen): "
    else:
        prompt += ": "

    location_id = get_integer_input(prompt, 1, len(locations), optional=optional)
    return location_id - 1 if location_id is not None else None


def get_printer_index_input(location: Location) -> int:
    """Zeigt Drucker eines Standorts an und fragt den Index ab."""
    cli_output.print_location_overview(location)

    if not location.printers:
        return None

    printer_id = get_integer_input("Drucker auswählen: ", 1, len(location.printers))
    return printer_id - 1


def input_printer_data(locations: List[Location]) -> Tuple[Dict[str, Any], str]:
    """Fragt alle Daten für einen neuen Drucker ab."""
    print("\n--- Neuen Drucker anlegen ---")
    location_idx = get_location_index_input(locations)
    location_name = locations[location_idx].name

    printer_data = {
        "dns": get_generic_input(
            "DNS-Namen/IP-Adresse des Druckers eingeben: ", empty=False
        ),
        "name": get_generic_input("Anzeigenamen des Druckers eingeben: ", empty=False),
        "model": get_generic_input("Modell des Druckers eingeben: ", empty=False),
        "driver_name": get_generic_input(
            "Name des Druckertreibers eingeben: ", empty=False
        ),
        "driver_inf_path": get_generic_input(
            "Pfad zur .inf-Treiberdatei eingeben: ", empty=False
        ),
    }
    return printer_data, location_name


def select_printer_data(locations: List[Location]) -> Tuple[Printer, Location]:
    """Lässt den Benutzer einen Standort und dann einen Drucker auswählen."""
    print("\n--- Drucker auswählen ---")
    location_idx = get_location_index_input(locations)
    if location_idx is None:
        return None, None

    location = locations[location_idx]

    if not location.printers:
        cli_output.print_warning("An diesem Standort gibt es keine Drucker.")
        return None, None

    printer_idx = get_printer_index_input(location)
    if printer_idx is None:
        return None, None

    printer = location.printers[printer_idx]
    return printer, location
