def cross(origin, a, b):
    return (a[0] - origin[0]) * (b[1] - origin[1]) - (a[1] - origin[1]) * (b[0] - origin[0])


def hull(points):
    return _divide(sorted(set(points)), None, None)


def hull_steps(points):
    steps = []
    _divide(sorted(set(points)), steps, [])
    return steps


def _divide(pts, steps, rejected):
    if len(pts) <= 3:
        return _small(pts)

    mid = len(pts) // 2
    left = _divide(pts[:mid], steps, rejected)
    right = _divide(pts[mid:], steps, rejected)
    return _merge(left, right, steps, rejected)


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


def _closed(chain):
    if len(chain) > 1:
        return list(chain) + [chain[0]]
    return list(chain)


def _merge(left, right, steps, rejected):
    if not left:
        return right
    if not right:
        return left
    if steps is not None:
        steps.append(("Teilung", [], [_closed(left), _closed(right)], list(rejected)))

    upper_i, upper_j = _tangent(left, right, True, steps, rejected)
    lower_i, lower_j = _tangent(left, right, False, steps, rejected)

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

    if rejected is not None:
        rejected.extend(_walk_edges(left, lower_i, upper_i))
        rejected.extend(_walk_edges(right, upper_j, lower_j))
    result = _drop_collinear(merged, rejected)
    if steps is not None:
        steps.append(("zusammengefügt", [], [_closed(result)], list(rejected)))
    return result


def _walk_edges(chain, start, end):
    edges = []
    if len(chain) < 2 or start == end:
        return edges
    i = start
    for _ in range(len(chain)):
        if i == end:
            break
        nxt = (i + 1) % len(chain)
        edges.append([chain[i], chain[nxt]])
        i = nxt
    return edges


def _farther(anchor, current, candidate):
    current_span = (current[0] - anchor[0]) ** 2 + (current[1] - anchor[1]) ** 2
    next_span = (candidate[0] - anchor[0]) ** 2 + (candidate[1] - anchor[1]) ** 2
    return next_span > current_span


def _keeps_going(anchor, current, candidate, upward):
    turn = cross(anchor, current, candidate)
    if upward:
        return turn > 0 or (turn == 0 and _farther(anchor, current, candidate))
    return turn < 0 or (turn == 0 and _farther(anchor, current, candidate))


def _tangent(left, right, upper, steps, rejected):
    n = len(left)
    m = len(right)
    if upper:
        i = max(range(n), key=lambda k: (left[k][0], left[k][1]))
        j = min(range(m), key=lambda k: (right[k][0], -right[k][1]))
        label = "obere Tangente"
    else:
        i = max(range(n), key=lambda k: (left[k][0], -left[k][1]))
        j = min(range(m), key=lambda k: (right[k][0], right[k][1]))
        label = "untere Tangente"

    def remember():
        if steps is not None:
            steps.append((
                label,
                [left[i], right[j]],
                [_closed(left), _closed(right), [left[i], right[j]]],
                list(rejected),
            ))

    for _ in range((n + m) * 2 + 2):
        remember()
        moved = False
        if upper:
            while _keeps_going(left[i], right[j], right[(j - 1) % m], True):
                j = (j - 1) % m
                moved = True
                remember()
            while _keeps_going(right[j], left[i], left[(i + 1) % n], False):
                i = (i + 1) % n
                moved = True
                remember()
        else:
            while _keeps_going(left[i], right[j], right[(j + 1) % m], False):
                j = (j + 1) % m
                moved = True
                remember()
            while _keeps_going(right[j], left[i], left[(i - 1) % n], True):
                i = (i - 1) % n
                moved = True
                remember()
        if not moved:
            break
    return i, j


def _drop_collinear(chain, rejected):
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
                if rejected is not None:
                    rejected.append([pts[(i - 1) % n], pts[i]])
                    rejected.append([pts[i], pts[(i + 1) % n]])
            else:
                keep.append(pts[i])
        if len(keep) < 3:
            return [min(pts), max(pts)]
        pts = keep
    return pts
