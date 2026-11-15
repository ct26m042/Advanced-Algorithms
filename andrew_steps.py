"""Andrew's Algorithmus - instrumentierte Version für den visuellen Modus.

Wird nur von view.py benutzt, NICHT für Zeitmessungen.
Die gemessene Version ist andrew.hull() in andrew.py.

Ein Schritt ist ein Tupel (text, hervorgehobene_punkte, linienzuege, verworfene_kanten).
"""


def cross(origin, a, b):
    return (a[0] - origin[0]) * (b[1] - origin[1]) - (a[1] - origin[1]) * (b[0] - origin[0])


def hull_steps(points):
    steps = []
    rejected = []
    pts = sorted(set(points))
    steps.append(("sortiert", [], [], []))
    if len(pts) <= 1:
        steps.append(("Hülle", list(pts), [], []))
        return steps

    lower = _side(pts, steps, "untere Kette", rejected)
    upper = _side(list(reversed(pts)), steps, "obere Kette", rejected)
    result = lower[:-1] + upper[:-1]
    steps.append(("Hülle", [], [result + [result[0]]], list(rejected)))
    return steps


def _side(points, steps, name, rejected):
    chain = []
    for point in points:
        while len(chain) >= 2 and cross(chain[-2], chain[-1], point) <= 0:
            dropped = chain.pop()
            rejected.append([chain[-1], dropped])
            steps.append((name + ": verworfen", [dropped], [list(chain)], list(rejected)))
        chain.append(point)
        steps.append((name, [point], [list(chain)], list(rejected)))
    return chain
