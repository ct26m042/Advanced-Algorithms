# Convex Hull – Assignment 1

## 1. Python installieren

Python 3.10 oder neuer von https://www.python.org/downloads/ installieren.
Beim Installieren **„Add python.exe to PATH“** anhaken.

## 2. Abhängigkeiten installieren

Im Projektordner ein Terminal öffnen:

```
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

## 3. Starten

```
.venv\Scripts\python convex_hull.py
```

## 4. Executable bauen (optional)

```
.venv\Scripts\python -m PyInstaller --onefile --console --add-data "data/hull;data/hull" convex_hull.py
```

Das Programm liegt danach in `dist/`.

## Probleme?

**`python` wird nicht gefunden:** `py` statt `python` verwenden.
