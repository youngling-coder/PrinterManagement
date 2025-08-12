# Drucker-Verwaltung – Benutzerhandbuch

## Überblick

**Drucker-Verwaltung** ist eine Windows-Anwendung zur zentralen Verwaltung und Installation von Netzwerkdruckern. Sie bietet eine grafische Oberfläche, mit der Sie Drucker und Standorte komfortabel anlegen, bearbeiten, installieren und entfernen können.

---

## Wichtiger Hinweis: Administrative Rechte

Für die Installation und Deinstallation von Druckern und Treibern sind Administratorrechte erforderlich. Starten Sie die Anwendung mit „Als Administrator ausführen“, um alle Funktionen nutzen zu können.

---

## 1. Hauptfenster und Bedienung

Das Hauptfenster gliedert sich in drei Bereiche:

- **Druckerübersicht (links):**  
  Zeigt alle Drucker nach Standorten gruppiert in einer Baumstruktur. Ein Suchfeld ermöglicht das schnelle Filtern nach Namen, Standort oder DNS/IP.

- **Detailansicht (rechts):**  
  Zeigt die Details des ausgewählten Druckers: Modell, Treibername, Treiberpfad, DNS/IP und Standort. Die Verfügbarkeitsprüfung zeigt, ob der Drucker im Netzwerk erreichbar ist.

- **Aktionsleiste (unten):**  
  Enthält Schaltflächen für:
  - **Erstellen:** Dropdown für neuen Standort oder Drucker.
  - **Bearbeiten & Löschen:** Ändern oder Entfernen des ausgewählten Eintrags.
  - **Installieren:** Startet die Installation eines verfügbaren Druckers.
  - **Fortschrittsbalken:** Zeigt den Status laufendes Prozesses.

---

## 2. Standorte und Drucker verwalten

### Standort anlegen

1. Klicken Sie auf „Erstellen...“ und wählen Sie „Standort“.
2. Geben Sie den Namen ein und bestätigen Sie mit „Erstellen“. Der Standort erscheint nun in der Druckerübersicht.

### Drucker hinzufügen

1. Wählen Sie „Erstellen...“ → „Drucker“.
2. Füllen Sie die Felder aus:
   - **Standort:** Auswahl aus bestehenden Standorten.
   - **Druckername:** Frei wählbar.
   - **Modell:** Hersteller/Modellbezeichnung.
   - **DNS/IP:** Netzwerkadresse des Druckers.
   - **Treibername:** Exakter Name aus der INF-Datei.
   - **Treiberpfad:** Klicken Sie ins Feld, um die `.inf`-Datei per Dialog auszuwählen (keine manuelle Eingabe).
3. Klicken Sie auf „Erstellen“, um den Drucker hinzuzufügen.

### Bearbeiten und Löschen

- Wählen Sie einen Eintrag aus und klicken Sie auf „Bearbeiten“ (Standort eines Druckers ist nachträglich nicht änderbar) oder „Löschen“.
- Standorte können nur gelöscht werden, wenn ihnen keine Drucker zugeordnet sind.

---

## 3. Drucker installieren

1. Wählen Sie einen Drucker in der Übersicht aus.
2. Prüfen Sie die Verfügbarkeit in der Detailansicht:
   - **JA (grün):** Drucker ist erreichbar, Installation möglich.
   - **NEIN (rot):** Drucker nicht erreichbar – prüfen Sie Netzwerk, Strom und DNS/IP.
3. Klicken Sie auf „Installieren“.
4. Der Fortschrittsbalken zeigt die drei Installationsschritte:
   1. TCP/IP-Port wird erstellt.
   2. Treiber wird registriert.
   3. Druckerinstanz wird angelegt und verknüpft.
5. Nach Abschluss erhalten Sie eine Erfolgs- oder Fehlermeldung.

---

## 4. Installierte Drucker verwalten

- Im Tab „Installierte Drucker“ sehen Sie alle lokal und im Netzwerk installierten Drucker.
- Mit „Aktualisieren“ laden Sie die Liste neu.
- Zur Deinstallation eines Druckers:
  1. Wählen Sie den Drucker aus.
  2. Klicken Sie auf „Deinstallieren“.
  3. Nach erfolgreicher Deinstallation erscheint eine Bestätigung, bei Fehlern eine entsprechende Meldung.

---

## Hilfe und Dokumentation

- Über das Menü „Hilfe“ können Sie die Online-Dokumentation direkt öffnen (`Strg+H`).

---

## Hinweise

- Die Anwendung prüft die Druckerverfügbarkeit automatisch und zeigt den Status in Echtzeit an.
- Für alle systemnahen Aktionen (Installation/Deinstallation) sind Administratorrechte erforderlich.