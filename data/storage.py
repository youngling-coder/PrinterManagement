# data/storage.py

import json
import os
import shutil
from typing import Dict, Any


# class Storage:
#     def __init__(self, filename: str):
#         self.backup_filepath = f"{filename}.bak"
#         if not os.path.exists(self.filepath):
#             # Erstellt eine leere JSON-Datei, wenn sie nicht existiert
#             with open(self.filepath, "w") as f:
#                 json.dump({}, f)

#     def load_data(self) -> Dict[str, Any]:
#         """Liest die JSON-Datei und gibt ihren Inhalt als Dictionary zurück."""
#         try:
#             with open(self.filepath, "r", encoding="utf-8") as f:
#                 return json.load(f)
#         except (json.JSONDecodeError, FileNotFoundError) as e:
#             raise FileNotFoundError(
#                 f"Konnte die Datendatei nicht laden: {self.filepath}. Fehler: {e}"
#             )

#     def save_data(self, data: Dict[str, Any]):
#         """Speichert das übergebene Dictionary als JSON."""
#         # 1. Zuerst ein internes Backup der aktuellen Datei erstellen
#         if os.path.exists(self.filepath):
#             shutil.copy2(self.filepath, self.backup_filepath)

#         # 2. Die neuen Daten schreiben
#         with open(self.filepath, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=4)

#     def create_manual_backup(self, backup_path: str):
#         """Erstellt ein Backup an einem benutzerdefinierten Ort."""
#         target_path = backup_path
#         if os.path.isdir(target_path):
#             target_path = os.path.join(
#                 target_path, os.path.basename(self.filepath) + ".bak"
#             )
#         shutil.copy2(self.filepath, target_path)

#     def restore_from_backup(self, backup_path: str):
#         """Stellt Daten aus einer Backup-Datei wieder her."""
#         if not os.path.exists(backup_path):
#             raise FileNotFoundError(f"Backup-Datei nicht gefunden: {backup_path}")
#         shutil.copy2(backup_path, self.filepath)
