"""Divide & Conquer konvexe Hülle - reine Version für den Performance-Modus.

Keine Schrittaufzeichnung, keine Visualisierung: diese Funktion wird gemessen.
Die instrumentierte Version für die Visualisierung liegt in divide_conquer_steps.py.
"""


def cross(origin, a, b):
    return (a[0] - origin[0]) * (b[1] - origin[1]) - (a[1] - origin[1]) * (b[0] - origin[0])


def hull(points):
    return _divide(sorted(set(points)))


def _divide(pts):
    if len(pts) <= 3:
        return _small(pts)

    mid = len(pts) // 2
    left = _divide(pts[:mid])
    right = _divide(pts[mid:])
    return _merge(left, right)


def _small(pts):
    if len(pts) <= 2:
        return list(pts)
    a, b, c = pts
    turn = cross(a, b, c)
    if turn == 0:
        return [a, c]
    if turn > 0:
        return [a, b, c]
    return [a, c, b]


def _merge(left, right):
    if not left:
        return right
    if not right:
        return left

    upper_i, upper_j = _tangent(left, right, True)
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

    return _drop_collinear(merged)


def _farther(anchor, current, candidate):
    current_span = (current[0] - anchor[0]) ** 2 + (current[1] - anchor[1]) ** 2
    next_span = (candidate[0] - anchor[0]) ** 2 + (candidate[1] - anchor[1]) ** 2
    return next_span > current_span


def _keeps_going(anchor, current, candidate, upward):
    turn = cross(anchor, current, candidate)
    if upward:
        return turn > 0 or (turn == 0 and _farther(anchor, current, candidate))
    return turn < 0 or (turn == 0 and _farther(anchor, current, candidate))


def _tangent(left, right, upper):
    n = len(left)
    m = len(right)
    if upper:
        i = max(range(n), key=lambda k: (left[k][0], left[k][1]))
        j = min(range(m), key=lambda k: (right[k][0], -right[k][1]))
    else:
        i = max(range(n), key=lambda k: (left[k][0], -left[k][1]))
        j = min(range(m), key=lambda k: (right[k][0], right[k][1]))

    for _ in range((n + m) * 2 + 2):
        moved = False
        if upper:
            while _keeps_going(left[i], right[j], right[(j - 1) % m], True):
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
