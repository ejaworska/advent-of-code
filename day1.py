with open("day1.txt", "r") as f:
    puzzle_input = f.readline()
    puzzle_input = puzzle_input.strip("\n")


puzzle = puzzle_input + puzzle_input[0]

sum_puzzle = 0

for i in range(len(puzzle)-1):
    if int(puzzle[i]) == int(puzzle[i+1]):
        sum_puzzle += int(puzzle[i])

print(sum_puzzle)
