def cross(origin, a, b):
    return (a[0] - origin[0]) * (b[1] - origin[1]) - (a[1] - origin[1]) * (b[0] - origin[0])


def hull(points):
    return _chain(points, None)


def hull_steps(points):
    steps = []
    _chain(points, steps)
    return steps


def _chain(points, steps):
    pts = sorted(set(points))
    rejected = []
    if steps is not None:
        steps.append(("sortiert", [], [], []))
    if len(pts) <= 1:
        if steps is not None:
            steps.append(("Hülle", list(pts), [], []))
        return pts

    lower = _side(pts, steps, "untere Kette", rejected)
    upper = _side(reversed(pts), steps, "obere Kette", rejected)
    result = lower[:-1] + upper[:-1]
    if steps is not None:
        closed = result + [result[0]] if len(result) > 1 else result
        steps.append(("Hülle", [], [closed], list(rejected)))
    return result


def _side(points, steps, name, rejected):
    chain = []
    for point in points:
        while len(chain) >= 2 and cross(chain[-2], chain[-1], point) <= 0:
            dropped = chain[-1]
            rejected.append([chain[-2], dropped])
            chain.pop()
            if steps is not None:
                steps.append((name + ": verworfen", [dropped], [list(chain)], list(rejected)))
        chain.append(point)
        if steps is not None:
            steps.append((name, [point], [list(chain)], list(rejected)))
    return chain
