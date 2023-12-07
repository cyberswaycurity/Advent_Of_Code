import re

with open("../inputs/puzzle-input","r") as f:
    lines = [line.strip() for line in f.readlines()]

columns = len(lines[0])
rows = len(lines)

number_candidates = dict()
gear_coordinates = []

for idx,line in enumerate(lines):

    num_indexes = re.finditer(r"\d+",line)

    for i in num_indexes:

        for j in range(i.start(),i.end()):

            number_candidates[(idx,j)] = int(line[i.start():i.end()])

    for i,j in enumerate(line):

        if j == "*":

            gear_coordinates.append((idx,i))

gear_ratios_sum = 0

for i in gear_coordinates:

    count = 0

    gear_ratio = 1

    row = i[0]
    col = i[1]

    checked_numbers = []

    for j in [(row - 1,col),(row - 1,col - 1),(row - 1,col + 1),(row,col - 1),(row,col + 1),(row + 1,col),(row + 1,col - 1),(row + 1,col + 1)]:

        if j in number_candidates.keys():

            if number_candidates[j] in checked_numbers:

                continue

            else:

                checked_numbers.append(number_candidates[j])
                gear_ratio = gear_ratio * number_candidates[j]
                count = count + 1

        if count == 2:

            break

    if count == 2:

        gear_ratios_sum = gear_ratios_sum + gear_ratio

print(gear_ratios_sum)
