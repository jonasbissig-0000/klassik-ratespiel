# CHRONOS – Klassik-Hitster (5-Karten-Prototyp)

## Testen
Öffne `index.html` im Browser. Wähle eine Karte oder verwende `index.html?karte=003`.

## Auf GitHub Pages veröffentlichen
1. Erstelle auf github.com ein **öffentliches** Repository namens `klassik-hitster`.
2. Lade **den Inhalt** dieses Ordners hoch (nicht den übergeordneten Ordner). Wichtig: `index.html`, `karten.html`, `audio/`, `karten.json` und `.nojekyll`.
3. Unter Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)` → Save.
4. Öffne `https://DEIN-NAME.github.io/klassik-hitster/?karte=001`.
5. Öffne `/karten.html`, prüfe die Basis-URL und drucke die QR-Karten.

## Musik austauschen
Ersetze `audio/001.wav` usw. durch **eigene rechtmässig nutzbare** Audiodateien mit denselben Dateinamen. Alternativ `karten.json` und die eingebettete Kartenliste in `index.html` anpassen (in dieser einfachen Version ist die Kartenliste für zuverlässiges lokales Öffnen eingebettet). Für grössere Sammlungen empfiehlt sich ein automatischer Generator aus CSV.

## Lizenz- und Datennotiz
Die beigefügten WAV-Dateien sind neu synthetisierte, vereinfachte Demonstrationen gemeinfreier Melodien; sie verwenden keine fremden Aufnahmen. Das Spiel hat keinen Login, keine Analysefunktionen und keinen eigenen Server. Die QR-Codes werden über den externen Dienst api.qrserver.com erzeugt; die Karten-URLs werden dafür an den Dienst übertragen. Die auf GitHub Pages hochgeladenen Audiodateien sind öffentlich abrufbar.

## Einschränkungen
Die Lösung ist im Browser technisch auslesbar; das Spiel setzt Fairplay voraus. Automatische Wiedergabe wird auf vielen Smartphones blockiert; daher muss auf Play getippt werden. Die Musikbeispiele sind bewusst nur eine technische Demo, keine künstlerisch überzeugenden Aufnahmen.
