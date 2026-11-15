# Convex Hull – Assignment 1

## 1. Python installieren

Python 3.10 oder neuer von https://www.python.org/downloads/ installieren.
Beim Installieren **„Add python.exe to PATH“** anhaken.

## 2. Abhängigkeiten installieren

Im Projektordner ein Terminal (cmd) öffnen:

```
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

## 3. Testdaten erzeugen

Die Dateien bis 64k Punkte liegen schon in `data/hull`. Die großen Dateien (128k bis 1M) sind nicht im Repository und müssen einmal erzeugt werden:

```
.venv\Scripts\python generate_hull_data.py
```

Der Befehl muss im Projektordner ausgeführt werden. Er benutzt `tools/qhull/rbox.exe` und erzeugt:

- `data/hull/`: 1k bis 64k Punkte
- `data/large/`: 128k bis 1M Punkte

Pro Größe gibt es zwei Dateien: `rand…` (zufällige Punkte) und `circle…` (Punkte auf einem Kreis).

## 4. Programm benutzen

```
.venv\Scripts\python convex_hull.py
```

Das Programm fragt zwei Dinge ab. Zahl eintippen und Enter drücken:

```
Algorithmus:
  1  Andrew
  2  Divide and Conquer
> 1
Ausgabe:
  1  Konsole
  2  visuell
> 1
```

**Konsole:** Der Algorithmus läuft über alle Testdateien und gibt pro Datei die Laufzeit aus. Fehlende Dateien werden übersprungen. Mit Enter schließen.

**Visuell:** Ein Fenster zeigt den Algorithmus Schritt für Schritt.

| Taste | Aktion |
| --- | --- |
| Leertaste oder Pfeil rechts | nächster Schritt |
| Esc | beenden |

## 5. Executable bauen (optional)

```
.venv\Scripts\python -m PyInstaller --onefile --console --add-data "data/hull;data/hull" convex_hull.py
```

Das Programm liegt danach in `dist/convex_hull.exe` und läuft per Doppelklick oder in cmd ohne Python. Die Dateien aus `data/hull` sind eingepackt.

## Mit make (optional)

Statt der Befehle oben gehen auch diese Abkürzungen. Dafür muss GNU make installiert sein, z. B. mit `winget install ezwinports.make`.

```
make install    Abhängigkeiten installieren
make data       große Testdaten erzeugen
make run        Programm starten
make test       Tests ausführen
make exe        Executable bauen
make clean      Build-Ordner löschen
```

## Probleme?

**`python` wird nicht gefunden:** `py` statt `python` verwenden.
