"""Andrew's Algorithmus (Monotone Chain) - eigene Implementierung.

Diese Funktion wird im Performance-Modus gemessen. Deshalb hier:
keine Visualisierung, kein print, keine Schrittaufzeichnung.
(Die Visualisierung nutzt andrew_steps.py.)

Vertrag - genau das prüft test_hull.py:
  Eingabe:  Liste von Punkten als (x, y)-Tupel. Die Liste darf NICHT verändert werden.
  Ausgabe:  neue Liste mit den Eckpunkten der konvexen Hülle,
            - gegen den Uhrzeigersinn (counter-clockwise),
            - beginnend beim kleinsten Punkt (kleinstes x, bei Gleichstand kleinstes y),
            - ohne Duplikate,
            - ohne kollineare Punkte auf den Kanten (nur echte Ecken).
  Sonderfälle: []           -> []
               ein Punkt    -> [p]
               alle Punkte auf einer Linie -> [kleinster Punkt, größter Punkt]

Testen:
  python -m unittest -v test_hull.TestAndrew
"""


def hull(points):
    raise NotImplementedError("Andrew's Algorithmus ist noch nicht implementiert (siehe andrew.py)")
