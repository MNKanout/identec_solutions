'''Sums up intgers from a text file'''
import os


def get_integers_from_file(file_path):
    '''Get integers from text file'''
    if not os.path.isfile(file_path):
        raise (FileNotFoundError('No file with integers was found!'))

    integers = []  # List containing all integers.
    with open(file_path) as f:
        for line in f.readlines():
            try:  # Add only integers to list.
                integers.append(int(line.rstrip("\n")))
            except ValueError:
                pass

    return integers


def sum_integers(file_path):
    '''Sum up integers from a text file'''
    integers = get_integers_from_file(file_path)
    return sum(integers)


if __name__ == '__main__':
    sum_integers('numbers.txt')
