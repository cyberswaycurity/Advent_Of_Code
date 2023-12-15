import sys

file = sys.argv[1]

with open(file,"r") as f:

    lines = [ [ i for i in line.strip() ]for line in f.readlines() ]

image = [ [ [y,x] for x in range(len(lines[0])) ] for y in range(len(lines)) ]

idx = 0

expansion = 1000000

while idx < len(lines):

    if all( i == '.' for i in lines[idx] ):

        for i in range(idx,len(lines)):

            for j in image[i]:

                j[0] = j[0] + expansion - 1

    idx = idx + 1

idx = 0

while idx < len(lines[0]):

    if all( lines[y][idx] == '.' for y in range(len(lines)) ):

        for i in image:

            for j in range(idx,len(lines[0])):

                i[j][1] = i[j][1] + expansion - 1

    idx = idx + 1

galaxies = []

for y in range(len(lines)):

    for x in range(len(lines[0])):

        if lines[y][x] == '#':

            galaxies.append([y,x])

distances = []

while galaxies:

    y1,x1 = galaxies.pop(0)

    for g in galaxies:

        y2,x2 = g

        delta_y = abs(image[y1][x1][0] - image[y2][x2][0])
        delta_x = abs(image[y1][x1][1] - image[y2][x2][1])

        distances.append(delta_y + delta_x)

print(sum(distances))
