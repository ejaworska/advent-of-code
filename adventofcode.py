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


def main():
    print(give_the_solution_day_1_1("day1.txt"))
    print(give_the_solution_day_1_2("day1.txt"))
    print(give_the_solution_day_2_1("day2.txt"))
if __name__ == '__main__':
    main()
