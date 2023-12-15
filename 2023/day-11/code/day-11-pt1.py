import sys

file = sys.argv[1]

with open(file,"r") as f:

    lines = [ [ i for i in line.strip() ]for line in f.readlines() ]

idx = 0

while idx < len(lines):

    if all( i == '.' for i in lines[idx] ):

        extra_line = lines[idx].copy()
        lines.insert(idx,extra_line)
        idx = idx + 2
        continue

    idx = idx + 1

idx = 0
while idx < len(lines[0]):

    if all( lines[y][idx] == '.' for y in range(len(lines)) ):

        curr_idx = idx

        for y in range(len(lines)):

            lines[y].insert(curr_idx,'.')

        idx = idx + 2

        continue

    idx = idx + 1

galaxies = []

for y in range(len(lines)):

    for x in range(len(lines[0])):

        if lines[y][x] == '#':

            galaxies.append([y,x])

galaxy = None

distances = []

while galaxies:

    y1,x1 = galaxies.pop(0)

    for g in galaxies:

        y2,x2 = g

        distances.append(abs(y2-y1)+abs(x2-x1))

print(sum(distances))
