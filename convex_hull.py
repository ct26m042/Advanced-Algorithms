import time


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


if __name__ == "__main__":

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
