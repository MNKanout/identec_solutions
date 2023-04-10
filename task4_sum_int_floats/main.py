'''Sums up numbers from a text file'''
import os


def get_numbers_from_file(file_path):
    '''Get numbers from text file'''
    if not os.path.isfile(file_path):
        raise (FileNotFoundError('No file with numbers was found!'))

    numbers = []  # List containing all numbers.
    with open(file_path) as f:
        for line in f.readlines():
            try:  # Add only numbers to list.
                numbers.append(float(line.rstrip("\n")))
            except ValueError:
                pass

    return numbers


def sum_numbers(file_path):
    '''Sum up numbers from a text file'''
    numbers = get_numbers_from_file(file_path)
    return sum(numbers)


if __name__ == '__main__':
    sum_numbers('numbers.txt')
