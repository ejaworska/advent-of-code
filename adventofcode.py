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
    
    with open(file_name, "r") as my_file:
        list_of_rows = my_file.read().splitlines()
    list_of_lists = []
    for row in list_of_rows:
        list_of_lists.append(row.split(" "))
    valid = 0
    for list_ in list_of_lists:
        if len(list_) == len(set(list_)):
            valid += 1
    return valid





def main():
    #print(give_the_solution_day_1_1("day1.txt"))
    #print(give_the_solution_day_1_2("day1.txt"))
    #print(give_the_solution_day_2_1("day2.txt"))
    #print(give_the_solution_day_2_2("day2.txt"))
    #print(give_the_solution_day_3_1(23))
    #print(give_the_solution_day_3_2(361527))
    print(give_the_solution_day_4_1("day4.txt"))
if __name__ == '__main__':
    main()
