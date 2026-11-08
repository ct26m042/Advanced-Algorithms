WIDTH = 900
HEIGHT = 640
PAD = 48


def play(points, steps, title):
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)
    font = pygame.font.SysFont("segoeui", 20)
    clock = pygame.time.Clock()
    index = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_SPACE, pygame.K_RIGHT):
                    if steps and index < len(steps) - 1:
                        index += 1

        screen.fill((24, 28, 36))
        if steps:
            text, highlights, lines, dashed = steps[index]
            prefix = str(index + 1) + "/" + str(len(steps)) + "  "
            if index == len(steps) - 1:
                prefix = prefix + "fertig  "
        else:
            text = "keine Schritte"
            highlights = []
            lines = []
            dashed = []
            prefix = ""
        _draw_dashed(screen, points, dashed)
        _draw_lines(screen, points, lines)
        _draw_points(screen, points, highlights)
        label = font.render(prefix + text, True, (236, 236, 236))
        hint = font.render("Leertaste oder Rechts: weiter    Esc: Ende", True, (180, 180, 180))
        screen.blit(label, (PAD, 16))
        screen.blit(hint, (PAD, HEIGHT - 36))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def _bounds(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return min(xs), min(ys), max(xs), max(ys)


def _to_screen(point, bounds):
    min_x, min_y, max_x, max_y = bounds
    span_x = max_x - min_x or 1
    span_y = max_y - min_y or 1
    x = PAD + (point[0] - min_x) / span_x * (WIDTH - 2 * PAD)
    y = HEIGHT - PAD - (point[1] - min_y) / span_y * (HEIGHT - 2 * PAD - 28)
    return int(x), int(y)


def _draw_dashed(screen, points, lines):
    import pygame

    if not points:
        return
    bounds = _bounds(points)
    for chain in lines:
        if len(chain) < 2:
            continue
        mapped = [_to_screen(point, bounds) for point in chain]
        for start, end in zip(mapped, mapped[1:]):
            _dash(screen, start, end, (214, 126, 112))


def _dash(screen, start, end, color):
    import pygame

    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    length = (dx * dx + dy * dy) ** 0.5
    if length < 1:
        return
    ux = dx / length
    uy = dy / length
    dist = 0
    draw = True
    while dist < length:
        seg = 8 if draw else 6
        seg = min(seg, length - dist)
        if draw:
            pygame.draw.line(
                screen,
                color,
                (int(x1 + ux * dist), int(y1 + uy * dist)),
                (int(x1 + ux * (dist + seg)), int(y1 + uy * (dist + seg))),
                2,
            )
        dist += seg
        draw = not draw


def _draw_lines(screen, points, lines):
    import pygame

    if not points:
        return
    bounds = _bounds(points)
    for chain in lines:
        if len(chain) < 2:
            continue
        mapped = [_to_screen(point, bounds) for point in chain]
        pygame.draw.lines(screen, (96, 196, 214), False, mapped, 2)


def _draw_points(screen, points, highlights):
    import pygame

    if not points:
        return
    bounds = _bounds(points)
    marked = set(highlights)
    for point in points:
        pos = _to_screen(point, bounds)
        if point in marked:
            pygame.draw.circle(screen, (255, 196, 64), pos, 8)
        else:
            pygame.draw.circle(screen, (236, 236, 236), pos, 5)
