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

    print(sum_puzzle)



def give_the_solution_day_1_2(file_name):
    puzzle_input = return_string_from_file(file_name)

    items_ahead = int(len(puzzle_input)/2)

    puzzle = puzzle_input + puzzle_input[0:items_ahead]
    sum_puzzle = 0
    for i in range(len(puzzle_input)):
        if int(puzzle[i]) == int(puzzle[i+items_ahead]):
            sum_puzzle += int(puzzle[i])
    print(sum_puzzle)


def main():
    give_the_solution_day_1_1("day1.txt")
    give_the_solution_day_1_2("day1.txt")
if __name__ == '__main__':
    main()
