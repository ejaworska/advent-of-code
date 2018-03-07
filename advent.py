import itertools

def return_string_from_file(file_name):
    with open(file_name, "r") as f:
        line = f.readline()
        line = line.strip("\n")
        return line


def open_file_as_list_of_lines(file_name):
    with open(file_name, "r") as my_file:
        list_of_lines = my_file.read().splitlines()
    return list_of_lines


def split_lines_in_list(list_of_lines):
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].split("\t")
    return list_of_lines


def change_type_of_line_element_to_integer(list_of_lines):
    for line in list_of_lines:
        for i in range(len(line)):
            line[i] = int(line[i])
    return list_of_lines


def give_the_solution_day_2_2(file_name):
    """Find the only two numbers in each row where one evenly divides the other,
    where the result of the division operation is a whole number. Find those
    numbers on each line, divide them, and add up each line's result."""

    list_of_lines = open_file_as_list_of_lines(file_name)

    split_lines_in_list(list_of_lines)

    change_type_of_line_element_to_integer(list_of_lines)

    list_of_per = []# list of lists containing tuples
    for i in range(len(list_of_lines)):
        list_of_per.append(list(itertools.permutations(list_of_lines[i], 2)))

    division_results = []
    for list_ in list_of_per:
        for set_ in list_:
            if set_[0]%set_[1] == 0:
                division_results.append(set_[0]/set_[1])

    checksum = int(sum(division_results))
    print(list_of_per)



give_the_solution_day_2_2("day2.txt")
