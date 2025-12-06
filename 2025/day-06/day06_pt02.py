with open("input.txt") as f:

    puzzle = f.read().split('\n')[:-1]

puzzle = [p for p in puzzle]

numbers = puzzle[:-1]
operations = puzzle[-1].split()

solution = 0

ops_idx = 0

beg_number = True

interim = 0

for c in range(len(numbers[0])):

    if beg_number:

        operation = operations[ops_idx]

        if operation == '*':

            interim = 1

        else:
            interim = 0

        beg_number = False

    num = ''

    for r in range(len(numbers)):

        curr = numbers[r][c]

        num = num + curr

        if num == ' ' * len(numbers):

            beg_number = True


    if beg_number:

        ops_idx += 1
        solution += interim
        
    elif operation == '*':

        interim *= int(num)

    else:

        interim += int(num)

solution += interim
print(solution)
