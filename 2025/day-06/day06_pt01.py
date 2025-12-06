with open("input.txt") as f:

    puzzle = f.read().strip().split('\n')

puzzle = [p.strip().split() for p in puzzle]

numbers = puzzle[:-1]
operations = puzzle[-1]

solution = 0

for c in range(len(operations)):

    if operations[c] == '*':
        interim = 1

    else:
        interim = 0

    for r in range(len(numbers)):

        if operations[c] == '*':

            interim *= int(numbers[r][c])
        else:
            interim += int(numbers[r][c])

    solution += interim

print(solution)

        
