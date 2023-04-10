'''Generates integers and writes them into a text file'''


def generate_integers_file(file_name, int_range):
    '''Generate integers and write them into a text file'''
    f = open(file_name, "w")
    for num in range(1, int_range+1):
        f.writelines(f"{num}\n")  # Write each number in a new line.
    f.close()


if __name__ == '__main__':
    generate_integers_file('num_1_500.txt', 500)
