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


def split_lines_in_list(list_of_lines, char):
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].split(char)
    return list_of_lines


def change_type_of_line_element_to_integer(list_of_lines):
    for line in list_of_lines:
        for i in range(len(line)):
            line[i] = int(line[i])
    return list_of_lines



def give_the_solution_day_1_1(file_name):
    """The captcha requires you to review a sequence of digits (your puzzle input)
     and find the sum of all digits that match the next digit in the list. The list
      is circular, so the digit after the last digit is the first digit in the list."""

    puzzle_input = return_string_from_file(file_name)

    puzzle = puzzle_input + puzzle_input[0]

    sum_puzzle = 0

    for i in range(len(puzzle_input)):
        if int(puzzle[i]) == int(puzzle[i+1]):
            sum_puzzle += int(puzzle[i])

    return sum_puzzle


def give_the_solution_day_1_2(file_name):
    """Now, instead of considering the next digit, it wants you to consider the digit
    halfway around the circular list. If your list contains 10 items, only
    include a digit in your sum if the digit 10/2 = 5 steps forward matches it."""

    puzzle_input = return_string_from_file(file_name)

    items_ahead = int(len(puzzle_input)/2)

    puzzle = puzzle_input + puzzle_input[0:items_ahead]
    sum_puzzle = 0
    for i in range(len(puzzle_input)):
        if int(puzzle[i]) == int(puzzle[i+items_ahead]):
            sum_puzzle += int(puzzle[i])
    return sum_puzzle


def give_the_solution_day_2_1(file_name):
    """For each row, determine the difference between the largest value and the
    smallest value; the checksum is the sum of all of these differences."""

    list_of_lines = open_file_as_list_of_lines(file_name)

    split_lines_in_list(list_of_lines, "\t")

    change_type_of_line_element_to_integer(list_of_lines)

    list_of_diff = []
    for line in list_of_lines:
        diff = max(line) - min(line)
        list_of_diff.append(diff)

    checksum = sum(list_of_diff)
    return checksum


def give_the_solution_day_2_2(file_name):
    """Find the only two numbers in each row where one evenly divides the other,
    where the result of the division operation is a whole number. Find those
    numbers on each line, divide them, and add up each line's result."""

    list_of_lines = open_file_as_list_of_lines(file_name)

    split_lines_in_list(list_of_lines, "\t")

    change_type_of_line_element_to_integer(list_of_lines)

    list_of_per = []#list of lists containing tuples
    for i in range(len(list_of_lines)):
        list_of_per.append(list(itertools.permutations(list_of_lines[i], 2)))

    division_results = []
    for list_ in list_of_per:
        for set_ in list_:
            if set_[0]%set_[1] == 0:
                division_results.append(set_[0]/set_[1])

    checksum = int(sum(division_results)) # remove floating point
    return checksum



def give_the_solution_day_3_1(puzzle_input):
    n = int(puzzle_input ** (0.5)) # find number to make a square
    square = n**2 # find the greatest square for the puzzle_input

    if square == puzzle_input:
        steps = n - 1
    elif square < puzzle_input:
        r = puzzle_input - square
        if r > n:
            steps = (r - n) - 1
        elif r <= n:
            steps = r

    return steps


def give_the_solution_day_3_2(n):
    spiral = {}
    spiral[(0,0)] = 1

    NEIGHBORS = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
    DIRECTION = [(1,0), (0,1), (-1,0), (0,-1)] #Right Up Left Down

    spiral = {}               # Spiral dictionary
    spiral[(0,0)] = 1
    x,y = 0,0
    steps_in_row = 1          # times spiral extends in same direction
    second_direction = False  # spiral extends in same direction twice: False if first leg, True if second
    nstep = 0                 # number of steps in current direction
    step_direction = 0        # index of direction in DIRECTION

    while True:
        dx, dy = DIRECTION[step_direction]
        x, y = x + dx, y + dy
        total = 0
        for neighbor in NEIGHBORS:
            nx, ny = neighbor
            if (x+nx, y+ny) in spiral:
                total += spiral[(x+nx, y+ny)]

        print("X: {}, Y:{}, Total:{}".format(x,y,total))

        if total > n:
            return total
        spiral[(x,y)] = total
        nstep += 1
        if nstep == steps_in_row:
            nstep = 0
            step_direction = (step_direction + 1)% 4
            if second_direction:
                second_direction = False
                steps_in_row += 1
            else:
                second_direction = True


def give_the_solution_day_4_1(file_name):
    """A passphrase consists of a series of words (lowercase letters) separated by spaces.
    A valid passphrase must contain no duplicate words. How many passphrases are valid?"""
    list_of_lines = open_file_as_list_of_lines(file_na    me)
    list_of_lists = split_lines_in_list(list_of_line    s, " ")
    return check_valid_passphrases(list_of_lists)

    

def check_valid_passphrases(list_of_lists):
    valid = 0
    for list_ in list_of_lists:
        if len(list_) == len(set(list_)):
            valid += 1
    return valid



def give_the_solution_day_4_2(file_name):
    """A valid passphrase must contain no two words that are anagrams of each other.
    How many passphrases are valid?"""


    list_of_lines = open_file_as_list_of_lines(file_name)
    list_of_lists = split_lines_in_list(list_of_lines, " ")

    for list_ in list_of_lists:
        for i in range(len(list_)):
            list_[i] = "".join(sorted(list_[i]))


    return check_valid_passphrases(list_of_lists)



def give_the_solution_day_5_1(file_name):
    """The message includes a list of the offsets for each jump.
    Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one.
    Start at the first instruction in the list.
    The goal is to follow the jumps until one leads outside the list.
    After each jump, the offset increases by 1."""

    offsets_list = open_file_as_list_of_lines(file_name)

    for i in range(len(offsets_list)):
        offsets_list[i] = int(offsets_list[i])

    jump = 0
    index = 0
    offset = offsets_list[index]
    while True:
        try:
            jump += 1
            index += offset
            offsets_list[index - offset] += 1 # instruction is incremented to 1
            offset = offsets_list[index]
        except IndexError:
            print("The exit is reached in", jump, "jumps")
            break


def give_the_solution_day_5_2(file_name):
    """After each jump, if the offset was three or more, instead decrease it by 1.
    Otherwise, increase it by 1 as before."""

    offsets_list = open_file_as_list_of_lines(file_name)

    for i in range(len(offsets_list)):
        offsets_list[i] = int(offsets_list[i])

    jump = 0
    index = 0
    offset = offsets_list[index]

    while True:
        try:
            jump += 1
            index += offset
            if offsets_list[index - offset] >= 3:
                offsets_list[index - offset] -= 1
            else:
                offsets_list[index - offset] += 1
            offset = offsets_list[index]
        except IndexError:
            print("The exit is reached in", jump, "jumps")
            break


def main():
    print(give_the_solution_day_1_1("day1.txt"))
    print(give_the_solution_day_1_2("day1.txt"))
    print(give_the_solution_day_2_1("day2.txt"))
    print(give_the_solution_day_2_2("day2.txt"))
    #print(give_the_solution_day_3_1(361527))
    #print(give_the_solution_day_3_2(361527))
    print(give_the_solution_day_4_1("day4.txt"))
    print(give_the_solution_day_4_2("day4.txt"))
    give_the_solution_day_5_1("day5.txt")
    give_the_solution_day_5_2("day5.txt")


if __name__ == '__main__':
    main()
