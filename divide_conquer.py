"""
Divide & Conquer konvexe Hülle - reine Version für den Performance-Modus.

No bullshit, all speed.
"""


def cross(origin, a, b):
    return (a[0] - origin[0]) * (b[1] - origin[1]) - (a[1] - origin[1]) * (b[0] - origin[0])


def hull(points):
    return _divide(sorted(set(points))) # duplikate entfernen und sortieren. PowerSort (MergeSort Variante) O(n log n). Set benutzt eine Hashtable für O(1) Lookup.


def _divide(pts):
    if len(pts) <= 3: # nur 3 Punkte sind immer konvex, daher direkt berechnen.
        return _small(pts)

    mid = len(pts) // 2 # index der mitte. 5 // 2 = 2.5 -> 2
    left = _divide(pts[:mid]) # aufteilung in zwei hälften für rekursion. an x-achse.
    right = _divide(pts[mid:])
    return _merge(left, right)


def _small(pts): # Nach rekursionen, die nur 2 oder 3 Punkte zurückgeben, wird die Hülle berechnet. Endlich ;'( 
    if len(pts) <= 2:
        return list(pts) # 2 Sind Konvex -> direkt zurückgeben.
    a, b, c = pts # 3 Punkte sind auch Konvex
    turn = cross(a, b, c) # Winkel zwischen a, b und c. Kreuzprodukt.
    if turn == 0: 
        return [a, c] # auf einer Linie -> nur 2 Punkte zurückgeben.
    if turn > 0:
        return [a, b, c] # gegen den Uhrzeigersinn angeordnet -> direkt zurückgeben.
    return [a, c, b] # im Uhrzeigersinn angeordnet -> umdrehen.


def _merge(left, right): # merge zwei halben hüllen zu einer.
    if not left: 
        return right
    if not right:
        return left

    upper_i, upper_j = _tangent(left, right, True) # obere tangente finden. True = oben.
    lower_i, lower_j = _tangent(left, right, False)

    merged = []
    i = upper_i
    while True:
        merged.append(left[i])
        if i == lower_i:
            break
        i = (i + 1) % len(left)
    j = lower_j
    while True:
        merged.append(right[j])
        if j == upper_j:
            break
        j = (j + 1) % len(right)

    return _drop_collinear(merged) # entfernt Punkte die auf einer Linie liegen. Also auf der Hülle, aber keine Ecken.


def _farther(anchor, current, candidate): # Entfernt sich der Punkt vom Anchor?
    current_span = (current[0] - anchor[0]) ** 2 + (current[1] - anchor[1]) ** 2 # Abstand zum Anchor.
    next_span = (candidate[0] - anchor[0]) ** 2 + (candidate[1] - anchor[1]) ** 2 # Abstand zum Anchor.
    return next_span > current_span # Entfernt sich der Punkt vom Anchor?


def _keeps_going(anchor, current, candidate, upward): # Geht die Kante weiter nach der logik: Gegen den Uhrzeigersinn.
    turn = cross(anchor, current, candidate) # Winkel zwischen anchor, current und candidate.
    if upward:
        return turn > 0 or (turn == 0 and _farther(anchor, current, candidate))
    return turn < 0 or (turn == 0 and _farther(anchor, current, candidate)) # oben oder unten.


def _tangent(left, right, upper):
    n = len(left)
    m = len(right)
    if upper:
        i = max(range(n), key=lambda k: (left[k][0], left[k][1])) # max x-wert und y-wert. 
        j = min(range(m), key=lambda k: (right[k][0], -right[k][1])) # min x-wert und -y-wert.
    else:
        i = max(range(n), key=lambda k: (left[k][0], -left[k][1])) # max x-wert und -y-wert.
        j = min(range(m), key=lambda k: (right[k][0], right[k][1])) # min x-wert und y-wert.

    for _ in range((n + m) * 2 + 2): # maximal 2n + 2m schritte.
        moved = False
        if upper:
            while _keeps_going(left[i], right[j], right[(j - 1) % m], True): # obere tangente finden.
                j = (j - 1) % m
                moved = True
            while _keeps_going(right[j], left[i], left[(i + 1) % n], False):
                i = (i + 1) % n
                moved = True
        else:
            while _keeps_going(left[i], right[j], right[(j + 1) % m], False):
                j = (j + 1) % m
                moved = True
            while _keeps_going(right[j], left[i], left[(i - 1) % n], True):
                i = (i - 1) % n
                moved = True
        if not moved:
            break
    return i, j


def _drop_collinear(chain):
    pts = []
    for point in chain:
        if not pts or pts[-1] != point:
            pts.append(point)
    if len(pts) > 1 and pts[0] == pts[-1]:
        pts.pop()
    if len(pts) <= 2:
        return pts

    changed = True
    while changed and len(pts) > 2:
        changed = False
        keep = []
        n = len(pts)
        for i in range(n):
            if cross(pts[(i - 1) % n], pts[i], pts[(i + 1) % n]) == 0:
                changed = True
            else:
                keep.append(pts[i])
        if len(keep) < 3:
            return [min(pts), max(pts)]
        pts = keep
    return pts
