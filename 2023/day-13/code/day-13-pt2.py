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

        boolean_array = [  x == y for first,second in zip(first_half,second_half) for x,y in zip(first,second)]

        if boolean_array.count(False) == 1:

            horizontal_reflections.append(i)

            noHorizReflection = False

            break

    if not noHorizReflection:

        continue

    transposed = list(map(list,zip(*p)))

    for i in range(1,len(transposed)):

        first_half = transposed[:i][::-1]
        second_half = transposed[i:]

        boolean_array = [  x == y for first,second in zip(first_half,second_half) for x,y in zip(first,second)]

        if boolean_array.count(False) == 1:

            vertical_reflections.append(i)

            break

solution = sum(vertical_reflections) + 100 * sum(horizontal_reflections)

print(solution)
