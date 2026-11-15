"""Andrew's Algorithmus (Monotone Chain).

Diese Funktion wird im Performance-Modus gemessen. Deshalb hier:
keine Visualisierung, kein print, keine Schrittaufzeichnung.
(Die Visualisierung nutzt andrew_steps.py.)

Aufbau wie in "Real-Time Collision Detection":
  1. Punkte von links nach rechts sortieren.
  2. Obere Kette von links nach rechts bauen.
  3. Untere Kette von links nach rechts bauen.
  4. Beide Ketten zur Huelle verbinden.

Testen:
  python -m unittest -v test_hull.TestAndrew
"""


def cross(o, a, b):
    """Orientierungstests Formel als Code:

    > 0: b liegt links von der Linie o -> a  (Linkskurve)
    < 0: b liegt rechts davon                (Rechtskurve)
    = 0: alle drei Punkte liegen auf einer Linie
    """
    ux = a[0] - o[0]   # Schritt von o nach a, in x
    uy = a[1] - o[1]   # Schritt von o nach a, in y
    vx = b[0] - o[0]   # Schritt von o nach b, in x
    vy = b[1] - o[1]   # Schritt von o nach b, in y
    return ux * vy - uy * vx


def hull(points):
    # Schritt 1: Duplikate entfernen (set) und von links nach rechts sortieren.
    # Tupel werden zuerst nach x, bei gleichem x nach y sortiert.
    # sorted() liefert eine NEUE Liste, die Eingabe bleibt unveraendert.
    pts = sorted(set(points))

    # Punkte zählen, bei 0 oder 1 Punkt gibt es nichts zu verbinden.
    if len(pts) <= 1:
        return pts

    # Schritt 2: obere Kette, von links nach rechts "upper"
    # Liegt der neue Punkt LINKS von der letzten Kante?
    # (oder genau auf ihrer Linie?), war der letzte Kettenpunkt falsch -> entfernen.
    # "while" statt "if", weil evtl. mehrere Punkte entfernt werden muessen
    # Nach jedem pop wird mit der neuen letzten Kante erneut geprueft, bis p rechts liegt. Dann wird p angehaengt.
    # (Von hinten löschen).
    upper = []
    for p in pts:
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) >= 0:
            upper.pop()
        upper.append(p)

    # Schritt 3: untere Kette, ebenfalls von links nach rechts "lower", so kann man die selbe Liste verwenden.
    # Gespiegelt: entfernen, wenn der neue Punkt RECHTS liegt (oder auf der Linie).
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Schritt 4: verbinden, gegen den Uhrzeigersinn.
    # Untere Kette links -> rechts, dann obere Kette rueckwaerts (rechts -> links).
    # Der letzte Punkt jeder Kette ist der erste der anderen,
    # darum jeweils mit [:-1] weglassen, sonst kaeme er doppelt vor.
    upper.reverse()
    return lower[:-1] + upper[:-1]
