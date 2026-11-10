# CHRONOS – Klassik / Clásica (Version 2)

## Die neue Version auf GitHub veröffentlichen

1. Entpacke das ZIP.
2. Öffne dein GitHub-Repository `klassik-ratespiel` und lade **die Dateien aus dem ZIP** hoch (nicht den übergeordneten Ordner). Bei gleichnamigen Dateien die vorhandenen Versionen ersetzen. Falls GitHub beim Upload einen Konflikt meldet, die vorhandenen Dateien einzeln über das Stiftsymbol aktualisieren oder die neuen Dateien im Repository hochladen.
3. Die Dateien `index.html`, `karten.html` und `karten.json` liegen direkt im Hauptverzeichnis; `audio/001.wav` usw. bleiben im Unterordner `audio`.
4. Nach dem Commit läuft die veröffentlichte GitHub-Pages-Webseite wie bisher.

## Aufbau

- `index.html`: Zweisprachiger Player mit optionaler ausführlicher Lösung.
- `karten.html`: QR-Vorder- und Rückseiten für Testdruck. Für den Duplexdruck unbedingt zunächst eine Testseite drucken; die korrekte Wendekante hängt vom Drucker ab.
- `CHRONOS_Mastertabelle.xlsx`: Pflege der Kartendaten.
- `karten.json`: Daten für Website und Karten.
- `excel_zu_json.py`: Exportiert aus der Excel-Datei wieder `karten.json`, ohne Zusatzpakete.
- `audio/`: fünf synthetisierte Demo-Ausschnitte aus Version 1.

## Neue Stücke und Auflösungen

1. `CHRONOS_Mastertabelle.xlsx` öffnen, Einträge bearbeiten oder neue Zeilen hinzufügen.
2. In Spalte P kannst du die **vollständige Auflösung** als freien Text eingeben. Jede Zeile erscheint später ohne Feldbezeichnungen. Ein Zeilenumbruch innerhalb einer Excel-Zelle funktioniert mit Alt+Enter (Windows) bzw. Ctrl+Option+Return (Mac, je nach Excel-Version).
3. Wenn Spalte P leer bleibt, erzeugt die Webseite die Auflösung automatisch aus Komponist, Werktitel, Satz, Jahr und den **Namen** in Spalten Q, R, S. Ohne «Dirigent:» usw. Leere Namensfelder erscheinen nicht.
4. Im Terminal im entpackten Ordner `python3 excel_zu_json.py CHRONOS_Mastertabelle.xlsx` ausführen.
5. Die neu erstellte `karten.json` sowie neue Audio-Dateien auf GitHub hochladen.

## Beispiel für Spalte P (Auflösung)

Giuseppe Verdi
Messa da Requiem
Introitus: Requiem aeternam
Herbert von Karajan
Wiener Philharmoniker

**Wichtig:** Trage die Namen nur dann ein, wenn sie zu der konkreten Aufnahme gehören. Die fünf synthetischen Demodateien sind keine Einspielungen eines Orchesters mit Dirigent oder Solisten; ihre Namensspalten bleiben daher leer.

## Audio und Rechte

Die fünf Audiodateien sind synthetische Funktionsbeispiele. Für das eigentliche Spiel rechtmässig nutzbare Einspielungen beschaffen und Lizenz bzw. Quelle in der Tabelle dokumentieren. Über GitHub Pages veröffentlichte Dateien sind grundsätzlich öffentlich zugänglich.

## Hinweise

Der QR-Code verweist auf die Karten-ID, nicht auf die Musikdatei. Beim Austausch einer Aufnahme bleibt die gedruckte Karte gültig. Die Karte `?karte=003` findet weiterhin Eintrag `003`. `karten.html` verwendet für die QR-Bilder den externen Dienst api.qrserver.com. Die QR-URLs werden an diesen Dienst übermittelt.

Die fünf Werkdaten dienen der technischen Demo; vor dem endgültigen Druck Datierungen und Werktitel redaktionell prüfen.
