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
    (128000, '128k'),
    (256000, '256k'),
    (512000, '512k'),
    (1000000, '1M'),
    (2000000, '2M'),
    (4000000, '4M'),
    (8000000, '8M'),
    (16000000, '16M'),
    (32000000, '32M'),
    (64000000, '64M'),
    (128000000, '128M'),
]


def main():
    rbox = shutil.which('rbox')
    if rbox is None:
        print('rbox wurde nicht gefunden.\n'
              'Bitte Qhull installieren und rbox in den PATH aufnehmen.')
        raise SystemExit(1)

    for n, label in SIZES:
        if n <= 64000:
            out_dir = os.path.join('data', 'hull')
        else:
            out_dir = os.path.join('data', 'large')
        os.makedirs(out_dir, exist_ok=True)
        for name, args in (
            ('rand', [str(n), 'D2']),
            ('circle', [str(n), 's', 'D2']),
        ):
            path = os.path.join(out_dir, name + label + '.txt')
            print(path)
            file = open(path, 'wb')
            result = subprocess.run([rbox] + args, stdout=file, stderr=subprocess.PIPE)
            file.close()
            if result.returncode != 0:
                print(result.stderr.decode('utf-8', errors='replace'))
                raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
