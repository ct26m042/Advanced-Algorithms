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
]


def find_rbox():
    here = os.path.dirname(os.path.abspath(__file__))
    bundled = os.path.join(here, 'tools', 'qhull', 'rbox.exe')
    if os.path.isfile(bundled):
        return bundled
    return shutil.which('rbox')


def main():
    rbox = find_rbox()
    if rbox is None:
        print('rbox wurde nicht gefunden.\n'
              'Erwartet unter tools/qhull/rbox.exe.')
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
