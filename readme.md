build erzeugen:
python -m PyInstaller --onefile --console --add-data "data/hull;data/hull" convex_hull.py
oder wenn sich in data nichts geändert hat
python -m PyInstaller convex_hull.spec