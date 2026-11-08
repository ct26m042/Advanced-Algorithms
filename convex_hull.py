import time

VISUAL = False


def read_points(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    points = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) >= 2:
            points.append((float(parts[0]), float(parts[1])))
    return points


def run_hull_and_print_time(filename_or_points):
    if type(filename_or_points) is str:
        filename = filename_or_points
        points = read_points(filename)
        start = time.time()
        convex_hull(points)
        end = time.time()
        print(filename + ':', end - start, 's')
    else:
        points = filename_or_points
        start = time.time()
        points = convex_hull(points)
        end = time.time()
        return points


def convex_hull(points):

    # TODO: Hüllenalgorithmus hier implementieren

    return points


def show_example(points, hull):
    import matplotlib.pyplot as plt

    plt.scatter([p[0] for p in points], [p[1] for p in points])
    if hull:
        closed = list(hull) + [hull[0]]
        plt.plot([p[0] for p in closed], [p[1] for p in closed])
    plt.title('kleines Beispiel')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == "__main__":

    test_points = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
    soll = [(0, 0), (1, 0), (1, 1), (0, 1)]

    ist = run_hull_and_print_time(test_points)

    if VISUAL:
        show_example(test_points, ist)
    else:
        print('soll: ' + str(soll))
        print('ist:  ' + str(ist))

    if ist != soll:
        print('Deine Implementierung scheint NICHT zu funktionieren oder noch nicht fertig zu sein.\n'
              'Überprüfe die convex_hull Funktion!')

    else:
        print('Deine Implementierung scheint zu funktionieren! :-) \n'
              'Weiter mit den Datenfiles...\n')
        print('Hülle:')
        run_hull_and_print_time('data/hull/rand1k.txt')
        run_hull_and_print_time('data/hull/rand2k.txt')
        run_hull_and_print_time('data/hull/rand4k.txt')
        run_hull_and_print_time('data/hull/rand8k.txt')
        run_hull_and_print_time('data/hull/rand16k.txt')
        run_hull_and_print_time('data/hull/rand32k.txt')
        run_hull_and_print_time('data/hull/rand64k.txt')

        run_hull_and_print_time('data/hull/circle1k.txt')
        run_hull_and_print_time('data/hull/circle2k.txt')
        run_hull_and_print_time('data/hull/circle4k.txt')
        run_hull_and_print_time('data/hull/circle8k.txt')
        run_hull_and_print_time('data/hull/circle16k.txt')
        run_hull_and_print_time('data/hull/circle32k.txt')
        run_hull_and_print_time('data/hull/circle64k.txt')
