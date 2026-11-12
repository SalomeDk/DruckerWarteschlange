# 3D-Drucker-Warteschlange

Eine einfache grafische Anwendung mit Python und Tkinter, um 3D-Druckaufträge zu organisieren. Die Aufträge werden der Reihe nach verwaltet und automatisch in einer JSON-Datei gespeichert.

## Funktionen

- Druckaufträge mit Kundenname, Auftragsname und geschätzter Druckdauer hinzufügen
- Warteschlange mit Auftragsnummer, Auftragsangaben, Status und Fortschrittsbalken anzeigen
- Wartende Aufträge mit vollem Balken darstellen; der Balken des aktiven Auftrags leert sich während der Druckzeit
- Nach Ablauf der eingetragenen Druckdauer abfragen, ob der Druck fertig ist
- Bei bestätigtem Abschluss den Auftrag entfernen und automatisch mit dem nächsten fortfahren
- Aufträge auswählen und nach einer Sicherheitsabfrage löschen; beim Löschen des aktiven Auftrags dessen Timer abbrechen
- Aufträge automatisch in `druckauftraege.json` speichern und beim nächsten Programmstart wieder laden

## Voraussetzungen

- Python 3
- Tkinter für die grafische Oberfläche
- `collections.deque`, `json`, `time`, `math` und `pathlib` aus der Python-Standardbibliothek

Es werden keine zusätzlichen Python-Pakete benötigt. Tkinter ist bei vielen Python-Installationen bereits enthalten. Falls Tkinter auf deinem System fehlt, installiere das Tkinter-Paket über die für dein Betriebssystem vorgesehene Python-Installation.

## Installation und Start

1. Lade das Projekt herunter oder klone das Repository.
2. Öffne ein Terminal im Ordner mit der Python-Datei.
3. Starte das Programm:

```bash
python 3d_printer_warteschlange.py
```

Je nach Betriebssystem und Python-Installation kann der Befehl stattdessen lauten:

```bash
python3 3d_printer_warteschlange.py
```

Unter Windows ist häufig auch dieser Aufruf möglich:

```powershell
py -3 3d_printer_warteschlange.py
```

## Bedienung

1. Klicke auf **„Auftrag hinzufügen“**.
2. Trage deinen Namen, den Auftragsnamen und die geschätzte Druckdauer in Sekunden ein. Alle Felder sind erforderlich; die Dauer muss größer als null sein.
3. Speichere den Auftrag. Er erscheint in der Tabelle. Der erste Auftrag startet automatisch, weitere Aufträge werden der Reihe nach eingereiht.
4. Der Fortschrittsbalken rechts zeigt bei wartenden Aufträgen den vollen Zustand. Beim aktiven Auftrag leert er sich kontinuierlich über die eingetragene Dauer.
5. Wähle zum Löschen einen Auftrag in der Tabelle aus und klicke auf das Papierkorb-Symbol. Bestätige die Sicherheitsabfrage.
6. Wenn die Zeit des aktiven Auftrags abgelaufen ist, fragt das Programm **„Druck abgeschlossen?“**. Mit **Ja** wird der Auftrag entfernt und der nächste startet. Mit **Nein** beginnt die Zeit für diesen Auftrag erneut und sein Balken füllt sich wieder.

## Speichern der Warteschlange

Die Anwendung legt `druckauftraege.json` automatisch neben der Python-Datei an. Sie speichert die Warteschlange beim Hinzufügen und Löschen von Aufträgen sowie nach einem bestätigten Abschluss. Beim nächsten Start werden die gespeicherten Aufträge wieder geladen.

Ein Auftrag, der beim Schließen der Anwendung gerade aktiv war, wird beim nächsten Start mit seiner vollen Druckdauer erneut gestartet. Der bisherige Timer-Fortschritt wird nicht gespeichert.

## Hinweise

Der Timer dient ausschließlich der Zeitüberwachung. Nach Ablauf der eingetragenen Dauer wird die Fertigstellung manuell abgefragt. Das Programm verbindet sich nicht mit einem 3D-Drucker und steuert, startet oder stoppt keinen Druck.

## Projektstruktur

```text
3D-Drucker-Warteschlange/
├── 3d_printer_warteschlange.py  # Python-Anwendung
├── druckauftraege.json          # wird beim ersten Speichern automatisch angelegt
└── README.md                    # Projektbeschreibung und Anleitung
```
