import os
import shutil
import subprocess


SIZES = [
    (1000, '1k'),
    (2000, '2k'),
    (4000, '4k'),
    (8000, '8k'),
    (16000, '16k'),
    (32000, '32k'),
    (64000, '64k'),
]


def main():
    rbox = shutil.which('rbox')
    if rbox is None:
        print('rbox wurde nicht gefunden.\n'
              'Bitte Qhull installieren und rbox in den PATH aufnehmen.')
        raise SystemExit(1)

    out_dir = os.path.join('data', 'hull')
    os.makedirs(out_dir, exist_ok=True)

    for n, label in SIZES:
        for name, args in (
            ('rand', [str(n), 'D2']),
            ('circle', [str(n), 's', 'D2']),
        ):
            result = subprocess.run(
                [rbox] + args,
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print(result.stderr)
                raise SystemExit(result.returncode)
            path = os.path.join(out_dir, name + label + '.txt')
            file = open(path, 'w')
            file.write(result.stdout)
            file.close()
            print(path)


if __name__ == "__main__":
    main()
