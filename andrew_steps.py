"""Andrew's Algorithmus - Version fuer den visuellen Modus.

Wird nur von view.py benutzt, NICHT fuer Zeitmessungen.
Gleicher Aufbau wie hull() in andrew.py, Schritt fuer Schritt.
Zusaetzlich wird nach jedem append und pop ein Bild fuer die Anzeige gespeichert.

Ein Schritt ist ein Tupel (text, gelbe_punkte, linien, gestrichelte_linien):
  text                 Beschriftung oben im Fenster
  gelbe_punkte         Punkte, die gelb markiert werden
  linien               Liste von Punktlisten, als durchgezogene Linien gezeichnet
  gestrichelte_linien  verworfene Kanten, gestrichelt gezeichnet
"""

from andrew import cross


def hull_steps(points):
    steps = []      # alle Bilder fuer die Anzeige
    rejected = []   # verworfene Kanten, bleiben gestrichelt sichtbar

    # Schritt 1: Duplikate entfernen und von links nach rechts sortieren.
    pts = sorted(set(points))
    steps.append(("sortiert", [], [], []))

    # Punkte zaehlen, bei 0 oder 1 Punkt gibt es nichts zu verbinden.
    if len(pts) <= 1:
        steps.append(("Huelle", list(pts), [], []))
        return steps

    # Schritt 2: obere Kette, von links nach rechts.
    # Entfernen, solange der neue Punkt LINKS der letzten Kante liegt (>= 0).
    upper = []
    for p in pts:
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) >= 0:
            dropped = upper.pop()
            rejected.append([upper[-1], dropped])
            steps.append(("obere Kette: verworfen", [dropped, p], [list(upper)], list(rejected)))
        upper.append(p)
        steps.append(("obere Kette", [p], [list(upper)], list(rejected)))

    # Schritt 3: untere Kette, ebenfalls von links nach rechts.
    # Gespiegelt: entfernen, wenn der neue Punkt RECHTS liegt (<= 0).
    # Die fertige obere Kette wird dabei weiter angezeigt.
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            dropped = lower.pop()
            rejected.append([lower[-1], dropped])
            steps.append(("untere Kette: verworfen", [dropped, p], [list(upper), list(lower)], list(rejected)))
        lower.append(p)
        steps.append(("untere Kette", [p], [list(upper), list(lower)], list(rejected)))

    # Schritt 4: verbinden, gegen den Uhrzeigersinn.
    # Untere Kette, dann obere Kette rueckwaerts, doppelte Endpunkte weglassen.
    upper.reverse()
    result = lower[:-1] + upper[:-1]
    steps.append(("Huelle", [], [result + [result[0]]], list(rejected)))
    return steps
