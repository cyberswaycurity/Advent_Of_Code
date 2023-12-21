import sys
import re

file = sys.argv[1]

with open(file,"r") as f:

    patterns = f.read()

patterns = re.split(r'\n\n',patterns)

patterns = [ [ [ c for c in i ] for i in p.split() ] for p in patterns ]

vertical_reflections = []

horizontal_reflections = []

for p in patterns:

    noHorizReflection = True

    for i in range(1,len(p)):

        first_half = p[:i][::-1]
        second_half = p[i:]

        if all(first == second for first,second in zip(first_half,second_half)):

            horizontal_reflections.append(i)

            noHorizReflection = False

            break

    if not noHorizReflection:

        continue

    transposed = list(map(list,zip(*p)))

    for i in range(1,len(transposed)):

        first_half = transposed[:i][::-1]
        second_half = transposed[i:]

        if all(first == second for first,second in zip(first_half,second_half)):

            vertical_reflections.append(i)

solution = sum(vertical_reflections) + 100 * sum(horizontal_reflections)

print(solution)
