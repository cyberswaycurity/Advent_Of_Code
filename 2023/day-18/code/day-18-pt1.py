import sys

file = sys.argv[1]

directions = { 'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0) }

with open(file,"r") as f:
    lines = [ line.split() for line in f.readlines() ]

perimeter_boundary = list()

y,x = (0,0)
perimeter = 0

for d,m,c in lines:

    perimeter = perimeter + int(m)

    y = y + ( directions[d][0] * int(m) )

    x = x + ( directions[d][1] * int(m) )

    perimeter_boundary.append((y,x))


# Surveyor's Theorem
# https://www.math.kent.edu/~soprunova/MST/projects/Johnson%20Spring%202021

perimeter_boundary.append(perimeter_boundary[0])
interior_points = 0

for i in range(0,len(perimeter_boundary)-1):

    y1,x1 = perimeter_boundary[i]
    y2,x2 = perimeter_boundary[i+1]

    interior_points = interior_points + ( (x1 * y2) - (x2 * y1) )

interior_points = int(interior_points / 2)

#Pick's Theorem
#https://en.wikipedia.org/wiki/Pick%27s_theorem

answer = interior_points + int(perimeter / 2) + 1

print(answer)
