# DruckerWarteschlange

Eine einfache grafische Anwendung mit Python und Tkinter, um 3D-Druckaufträge zu organisieren. Aufträge werden in einer Warteschlange angezeigt und der Reihe nach verwaltet.

## Funktionen

- Druckaufträge mit Kundenname, Auftragsname und geschätzter Druckdauer hinzufügen
- Warteschlange mit Auftragsnummer, Angaben zum Auftrag und Status anzeigen
- Den aktuell bearbeiteten Auftrag sowie wartende Aufträge unterscheiden
- Nach Ablauf der eingetragenen Druckdauer eine Abfrage anzeigen, ob der Druck fertig ist
- Aufträge in der Tabelle auswählen und nach einer Sicherheitsabfrage löschen
- Beim Löschen des aktuellen Auftrags dessen Timer abbrechen und mit dem nächsten Auftrag fortfahren

## Voraussetzungen

- Python 3
- Tkinter für die grafische Oberfläche
- `collections.deque` für die Warteschlange (Teil der Python-Standardbibliothek)

Es werden keine zusätzlichen Python-Pakete benötigt. Tkinter ist bei vielen Python-Installationen bereits enthalten. Falls Tkinter auf deinem System fehlt, installiere das Tkinter-Paket über die für dein Betriebssystem vorgesehene Python-Installation.

## Installation und Start

1. Lade das Projekt herunter oder klone das Repository.
2. Öffne ein Terminal im Projektordner.
3. Starte das Programm:

```bash
python main.py
```

Je nach Betriebssystem und Python-Installation kann der Befehl stattdessen lauten:

```bash
python3 main.py
```

Unter Windows ist häufig auch dieser Aufruf möglich:

```powershell
py -3 main.py
```

## Bedienung

1. Klicke auf **„Auftrag hinzufügen“**.
2. Trage deinen Namen, den Auftragsnamen und die geschätzte Druckdauer in Sekunden ein. Alle Felder sind erforderlich; die Dauer muss größer als null sein.
3. Speichere den Auftrag. Er erscheint in der Tabelle. Der erste Auftrag startet automatisch, weitere Aufträge werden der Reihe nach eingereiht.
4. Wähle zum Löschen einen Auftrag in der Tabelle aus und klicke auf das Papierkorb-Symbol. Bestätige die Sicherheitsabfrage.
5. Wenn die eingetragene Zeit des aktuellen Auftrags abgelaufen ist, fragt das Programm **„Druck abgeschlossen?“**. Bestätige mit **Ja**, um den Auftrag aus der Warteschlange zu entfernen und den nächsten zu starten. Bei **Nein** wartet der Timer die eingetragene Dauer erneut ab und fragt anschließend wieder nach.

## Hinweise

Der Timer dient ausschließlich der Zeitüberwachung. Nach Ablauf der eingetragenen Dauer wird die Fertigstellung manuell abgefragt. Das Programm verbindet sich nicht mit einem 3D-Drucker und steuert, startet oder stoppt keinen Druck.

Die Aufträge werden nur während der laufenden Programmsitzung im Arbeitsspeicher gehalten. Beim Schließen der Anwendung wird die Warteschlange nicht gespeichert.

## Projektstruktur

```text
3D-Drucker-Warteschlange/
├── main.py      # Python-Anwendung
└── README.md    # Projektbeschreibung und Anleitung
```
