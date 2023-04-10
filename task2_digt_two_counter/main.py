'''Counts the occurrences of digit "2" in numbers ranges from 1 to N'''


def count_digit_two(num):
    '''Count the occurrences of digit "2" in numbers from 1 to given number'''
    if not isinstance(num, int) or not num > 0:  # Range should be positive int
        raise ValueError('The input range has to be a positive integer.')
    numbers = list(range(1, num+1))  # List of numbers in the given range.
    # List all digits in the list as strings, and return count of digit "2".
    return list(str(numbers)).count("2")
