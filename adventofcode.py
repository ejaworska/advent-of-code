import itertools

def return_string_from_file(file_name):
    with open(file_name, "r") as f:
        line = f.readline()
        line = line.strip("\n")
        return line

def give_the_solution_day_1_1(file_name):
    puzzle_input = return_string_from_file(file_name)

    puzzle = puzzle_input + puzzle_input[0]

    sum_puzzle = 0

    for i in range(len(puzzle)-1):
        if int(puzzle[i]) == int(puzzle[i+1]):
            sum_puzzle += int(puzzle[i])

    return sum_puzzle



def give_the_solution_day_1_2(file_name):
    puzzle_input = return_string_from_file(file_name)

    items_ahead = int(len(puzzle_input)/2)

    puzzle = puzzle_input + puzzle_input[0:items_ahead]
    sum_puzzle = 0
    for i in range(len(puzzle_input)):
        if int(puzzle[i]) == int(puzzle[i+items_ahead]):
            sum_puzzle += int(puzzle[i])
    return sum_puzzle


def give_the_solution_day_2_1(file_name):
    with open(file_name, "r") as f:
        list_of_lines = f.read().splitlines()
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].split("\t")

    for line in list_of_lines:
        for i in range(len(line)):
            line[i] = int(line[i])

    list_of_diff = []
    for line in list_of_lines:
        diff = max(line) - min(line)
        list_of_diff.append(diff)

    checksum = sum(list_of_diff)
    return checksum

def give_the_solution_day_2_2(file_name):
    with open(file_name, "r") as f:
        list_of_lines = f.read().splitlines()

    list_of_rows = []
    for line in list_of_lines:
        list_of_rows.append(line.split("\t"))

    for line in list_of_rows:
        for i in range(len(line)):
            line[i] = int(line[i])

    list_of_per = []#lista zawierajća listy zawierające tuple
    for i in range(len(list_of_rows)):
        list_of_per.append(list(itertools.permutations(list_of_rows[i], 2)))

    division_results = []
    for list_ in list_of_per:
        for set_ in list_:
            if set_[0]%set_[1] == 0:
                division_results.append(set_[0]/set_[1])

    checksum = int(sum(division_results))
    return checksum




def main():
    #print(give_the_solution_day_1_1("day1.txt"))
    #print(give_the_solution_day_1_2("day1.txt"))
    #print(give_the_solution_day_2_1("day2.txt"))
    print(give_the_solution_day_2_2("day2.txt"))
if __name__ == '__main__':
    main()
