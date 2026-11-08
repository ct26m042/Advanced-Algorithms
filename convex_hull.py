import os
import random
import sys
import time

import andrew
import divide_conquer
import view


FILES = [
    "rand1k.txt",
    "rand2k.txt",
    "rand4k.txt",
    "rand8k.txt",
    "rand16k.txt",
    "rand32k.txt",
    "rand64k.txt",
    "rand128k.txt",
    "rand256k.txt",
    "rand512k.txt",
    "rand1M.txt",
    "rand2M.txt",
    "rand4M.txt",
    "rand8M.txt",
    "rand16M.txt",
    "rand32M.txt",
    "rand64M.txt",
    "rand128M.txt",
    "circle1k.txt",
    "circle2k.txt",
    "circle4k.txt",
    "circle8k.txt",
    "circle16k.txt",
    "circle32k.txt",
    "circle64k.txt",
    "circle128k.txt",
    "circle256k.txt",
    "circle512k.txt",
    "circle1M.txt",
    "circle2M.txt",
    "circle4M.txt",
    "circle8M.txt",
    "circle16M.txt",
    "circle32M.txt",
    "circle64M.txt",
    "circle128M.txt",
]


def data_dirs():
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
        return [os.path.join(base, "data", "hull")]
    base = os.path.dirname(os.path.abspath(__file__))
    return [
        os.path.join(base, "data", "hull"),
        os.path.join(base, "data", "large"),
    ]


def find_data_file(name):
    for folder in data_dirs():
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            return path
    return None


def read_points(filename):
    file = open(filename, "r")
    lines = file.readlines()
    points = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) >= 2:
            points.append((float(parts[0]), float(parts[1])))
    return points


def run_hull_and_print_time(filename, hull_fn):
    points = read_points(filename)
    start = time.time()
    hull_fn(points)
    end = time.time()
    folder = os.path.basename(os.path.dirname(filename))
    print("data/" + folder + "/" + os.path.basename(filename) + ":", end - start, "s")


def demo_points():
    rng = random.Random(1)
    return [(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(10)]


def ask(valid):
    while True:
        choice = input("> ").strip()
        if choice in valid:
            return choice
        print("Bitte " + " oder ".join(sorted(valid)) + " eingeben.")


def main():
    print("Algorithmus:")
    print("  1  Andrew")
    print("  2  Divide and Conquer")
    algo = ask({"1", "2"})

    print("Ausgabe:")
    print("  1  Konsole")
    print("  2  visuell")
    mode = ask({"1", "2"})

    if algo == "1":
        hull_fn = andrew.hull
        steps_fn = andrew.hull_steps
        title = "Andrew"
    else:
        hull_fn = divide_conquer.hull
        steps_fn = divide_conquer.hull_steps
        title = "Divide and Conquer"

    if mode == "1":
        print("Hülle:")
        for name in FILES:
            path = find_data_file(name)
            if path is None:
                continue
            run_hull_and_print_time(path, hull_fn)
        try:
            input("Enter zum Schließen...")
        except EOFError:
            pass
    else:
        points = demo_points()
        view.play(points, steps_fn(points), title)


if __name__ == "__main__":
    main()
