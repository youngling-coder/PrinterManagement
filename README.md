# Anwendngsdokumentation: Drucker Verwaltung

Dieses Program dient zur zentralen Verwaltung und Installation von Netzwerkdruckern. Es speichert alle konfigurationen in einer lokalen printers.json Datei und bietet zwei Betriebsmodi: eine graphische Benutzeroberfläche für intuitive Bedienung und ein Kommandozeilen-Interface für schnelle, skriptgesteurerte Aufgaben.

**Wichtiger Hinweis:** Die Installation von Druckertreibern erfordert administrative Rechte.

## 1. Grafische Benutzeroberfläche
Die GUI bietet eine visuelle und interaktive Methode zur Verwaltung Ihrer Drucker.

### 1.1 Starten der Anwendung
Führen Sie die  `DruckerVerwaltungGUI.exe` aus. Es öffnet sich das Hauptfenster der Anwendung.

### 1.2 Das Hauptfenster
Das Hauptfenster ist in drei Hauptvereiche unterteilt:

1. **Druckerübersicht (links)**
- Eine Baumansicht, die alle Drucker nach Standorte gruppiert anzeigt
- Standorte sind die Haupteinträge
- Über dem Baum befindet sich ein Suchfeld, mit dem Sie die Liste filtern können

2. **Detailansicht (rechts)**
- Zeigt detaillierte Informationen über den in der Übersicht ausgewählten Drucker an
- Wenn ein Standort oder kein Element ausgewählt ist, werden hier keine spezifischen Daten angezeigt

3. **Aktionsleiste (unten)**
- Forschrittsbalken: Zeigt den Status einer laufenden Druckerinstallation an
- Button "Installieren": Startet den Installationsvorgangfür den ausgewählten und verfügbaren Drucker
- Unter links befinden sich die Buttons "Löschen" und "Bearbeiten"
- Unter rechts befindet sich das Dropdown-Menü "Erstellen neunen...", um neue Drucker oder Standorte anzulegen

### 1.3 Standorte Verwalten

#### Einen neuen Standort erstellen
1. Auf das Dropdown-Menü **"Erstellen neuen..."** unten rechts klicken
2. Option **"Standort"** wählen
3. Den gewünschten Namen für den neuen Standort eingeben
4. Auf **"Erstellen"** klicken. Der neue Standort erscheint sofort in der Druckerübersicht

#### Einen Standort löschen

**Achtung:** Ein Standort kann nur gelöscht werden, wenn ihm keine Drucker mehr zugeordnet sind.

1. Den zu löschenden Standort in der Druckerübersicht auswählen
2. Auf den Button **"Löschen"** unten links
3. Die Sicherheitsabfrage bestätigen


### 1.4 Drucker verwalten

#### Einen neuen Drucker hinzufügen

1. Auf das Dropdown-Menü **"Erstellen neuen..."** klicken und **Drucker** wählen
2. Die folgenden Felder ausfüllen
- **Standard:** Aus der Dropdown-Liste den Standort, an dem der Drucker hinzugefügt werden soll, auswählen. (Falls die Liste leer ist, müssen Sie zuerst einen Standort erstellen)
- **Druckername:** Ein fre wählbarer Name, der in der Übersicht angezeigt wird. 
- **Druckermodell:** Das genaue Modell des Druckers
- **DNS-Name:** Der vollqualifizierte DNS-Name des Druckers im Netzwerk. (Kann auch eine IP-Adresse sein, aber **NICHT** empfohlen!)
- **Treibername:** Der exakte Name des Treibers, wie er in der .inf-Datei definiert ist (Standard: Canon Generic PCL6 Driver)
- **Treiberpfad:** Der Pfad zur .inf-Datei des Treibers. **Bitte den Pfad manuell nicht eingeben.** In dieses Feld klicken, um einen Dateiauswahldialog zu öffnen und zur richtigen .inf-Datei zu navigieren. (Standard: CNP60MA64.INF, **Bitte nicht ändern ohne Bedarf**)
4. Auf **"Erstellen"** klicken. Der Drucker wird dem gewählten Standort hinzugefügt.

#### Einen Drucker bearbeiten

1. Den zu bearbeitenden Drucker in der Übersicht auswählen
2. Auf den Button **"Bearbeiten"** Klicken
3. Die gewünschten Informationen ändern. Beachten Sie, dass der Standort nachträglich nicht geändert werden kann
4. Auf **"Übernehmen"** klicken, um Änderungen zu speichern

#### Einen Drucker löschen

1. Den zu löschenden Drucker in der Übersicht auswählen
2. Auf den Button **"Löschen"** klicken
3. Die Sicherheitsabfrage bestätigen

#### Druckerdetails und Verfügbarkeit prüfen

Wenn Sie einen Drucker in der Übersicht auswählen, werden seine Daten im rechten Detailbereich angezeigt. Die Anwendung führt automatisch eime Netzwerkprüfung durch:

- **PRÜFUNG LÄUFT...:** Die Anwendung versucht, den Drucker im Netzwerk zu erreichen
- **JA:** Der Drucker ist über das Netzwerk erreichbar. Der "Installieren"-Button wird aktiviert.
- **NEIN:** Der Drucker konnte nicht erreicht werden. Prüfen Sie die DNS/IP-Addresse und die Netzwerkverbindung. Prüfen Sie auch, ob der Drucker im aktuellen Netzwerk hinzugefügt wurde. Der "Installieren"-Button bleibt deaktiviert.

### 1.5 Einen Drucker installieren

1. Einen Drucker in der Übersicht auswählen
2. Sicherstellen, dass der Drucker Verfügbar ist (Verfügbar: JA)
3. Auf **"Installieren"** button klicken
4. Der Installationsprozess startet. Der Fortschrittsbalken zeigt die einzelnen Schritte an
- [Schritt 1/3]: Erstellt den TCP/IP-Port
- [Schritt 2/3]: Installiert den Druckertreiber im System
- [Schritt 3/3]: Erstellt die Druckerinstanz und verknüpft sie mit Port und Treiber
5. Nach Abschluss erhalten Sie eine Erfolgs- oder Fehlermeldung.

### 1.6 Suchen und Filtern

Geben Sie einen Suchbegriff in das Suchfeld über der Druckerübersicht ein. Die Liste wird in Echtzeit gefiltert und zeigt nur noch Standorte und Drucker an, die den Suchbegriff im namen entahlten.


## 2. Kommandozeilen-Interface 

### 2.1 Starten der Anwendung
Führen Sie die `DruckerVerwaltungCLI.exe`. Es öffnet sich das Hauptfenster der Anwendung.
