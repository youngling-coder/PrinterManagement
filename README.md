# Anwendngsdokumentation: Drucker Verwaltung

Dieses Program dient zur zentralen Verwaltung und Installation von Netzwerkdruckern. Es speichert alle konfigurationen in einer lokalen printers.json Datei und bietet zwei Betriebsmodi: eine graphische Benutzeroberfläche für intuitive Bedienung und ein Kommandozeilen-Interface für schnelle, skriptgesteurerte Aufgaben.

#### Wichtiger Hinweis: Die Installation von Druckertreibern erfordert administrative Rechte.

## 1. Grafische Benutzeroberfläche
Die GUI bietet eine visuelle und interaktive Methode zur Verwaltung Ihrer Drucker.

### 1.1 Starten der Anwendung
Führen Sie die DruckerVerwaltungGUI.exe aus. Es öffnet sich das Hauptfenster der Anwendung.

### 1.2 Das Hauptfenster
Das Hauptfenster ist in drei Hauptvereiche unterteilt:

1. Druckerübersicht (links)
- Eine Baumansicht, die alle Drucker nach Standorte gruppiert anzeigt
- Standorte sind die Haupteinträge
- Über dem Baum befindet sich ein Suchfeld, mit dem Sie die Liste filtern können

2. Detailansicht (Rechts):
- Zeigt detaillierte Informationen über den in der Übersicht ausgewählten Drucker an
- Wenn ein Standort oder kein Element ausgewählt ist, werden hier keine spezifischen Daten angezeigt

3. Aktionsleiste (unten):
- Forschrittsbalken: Zeigt den Status einer laufenden Druckerinstallation an
- Button "Installieren": Startet den Installationsvorgangfür den ausgewählten und verfügbaren Drucker
- Unter links befinden sich die Buttons "Löschen" und "Bearbeiten"
- Unter rechts befindet sich das Dropdown-Menü "Erstellen neunen...", um neue Drucker oder Standorte anzulegen
