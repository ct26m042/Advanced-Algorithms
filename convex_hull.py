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
    "circle1k.txt",
    "circle2k.txt",
    "circle4k.txt",
    "circle8k.txt",
    "circle16k.txt",
    "circle32k.txt",
    "circle64k.txt",
]


def hull_dir():
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "data", "hull")


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
    print("data/hull/" + os.path.basename(filename) + ":", end - start, "s")


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
        folder = hull_dir()
        for name in FILES:
            run_hull_and_print_time(os.path.join(folder, name), hull_fn)
        try:
            input("Enter zum Schließen...")
        except EOFError:
            pass
    else:
        points = demo_points()
        view.play(points, steps_fn(points), title)


if __name__ == "__main__":
    main()
