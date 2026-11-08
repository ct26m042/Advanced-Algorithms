import time


def read_file_into_array(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    arr = [int(n) for n in lines]
    return arr


def run_sort_and_print_time(filename_or_arr):
    if type(filename_or_arr) is str:
        filename = filename_or_arr
        arr = read_file_into_array(filename)
        start = time.time()
        sort(arr)
        end = time.time()
        print(filename + ':', end - start, 's')
    else:
        arr = filename_or_arr
        start = time.time()
        arr = sort(arr)
        end = time.time()
        return arr


def sort(arr):

    # TODO: Sortieralgorithmus hier implementieren

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

    return arr


if __name__ == "__main__":

    test_arr = run_sort_and_print_time([9, 2, 3, 2, 1, 7, 5, 9])

    print('soll: [1, 2, 2, 3, 5, 7, 9, 9]')
    print('ist:  ' + str(test_arr))

    if test_arr != [1, 2, 2, 3, 5, 7, 9, 9]:
        print('Deine Implementierung scheint NICHT zu funktionieren oder noch nicht fertig zu sein.\n'
              'Überprüfe die sort Funktion!')

    else:
        print('Deine Implementierung scheint zu funktionieren! :-) \n'
              'Weiter mit den Datenfiles...\n')
        print('Sortiere:')
        run_sort_and_print_time('data/desc1k.txt')
        run_sort_and_print_time('data/desc2k.txt')
        run_sort_and_print_time('data/desc4k.txt')
        run_sort_and_print_time('data/desc8k.txt')
        run_sort_and_print_time('data/desc16k.txt')
        run_sort_and_print_time('data/desc32k.txt')
        run_sort_and_print_time('data/desc64k.txt')

        run_sort_and_print_time('data/asc1k.txt')
        run_sort_and_print_time('data/asc2k.txt')
        run_sort_and_print_time('data/asc4k.txt')
        run_sort_and_print_time('data/asc8k.txt')
        run_sort_and_print_time('data/asc16k.txt')
        run_sort_and_print_time('data/asc32k.txt')
        run_sort_and_print_time('data/asc64k.txt')

        run_sort_and_print_time('data/rand1k.txt')
        run_sort_and_print_time('data/rand2k.txt')
        run_sort_and_print_time('data/rand4k.txt')
        run_sort_and_print_time('data/rand8k.txt')
        run_sort_and_print_time('data/rand16k.txt')
        run_sort_and_print_time('data/rand32k.txt')
        run_sort_and_print_time('data/rand64k.txt')
