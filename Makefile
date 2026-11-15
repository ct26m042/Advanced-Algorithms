# Makefile fuer Windows (cmd).
# Braucht GNU make, z. B. installieren mit:  winget install ezwinports.make
# Gleiche Befehle wie im README, nur kuerzer.

PY = ".venv/Scripts/python.exe"

.PHONY: help install data run test exe clean

help:
	@echo make install   Abhaengigkeiten installieren
	@echo make data      grosse Testdaten erzeugen
	@echo make run       Programm starten
	@echo make test      Tests ausfuehren
	@echo make exe       Executable bauen, Ergebnis in dist
	@echo make clean     Build-Ordner loeschen

install:
	python -m venv .venv
	$(PY) -m pip install -r requirements.txt

data:
	$(PY) generate_hull_data.py

run:
	$(PY) convex_hull.py

test:
	$(PY) -m unittest -v test_hull

exe:
	$(PY) -m PyInstaller --noconfirm --onefile --console --add-data "data/hull;data/hull" convex_hull.py

clean:
	$(PY) -c "import shutil; shutil.rmtree('build', True); shutil.rmtree('dist', True)"
