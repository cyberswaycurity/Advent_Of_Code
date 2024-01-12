import sys

file = sys.argv[1]

directions = { '0':(0,1), '2':(0,-1), '3':(-1,0), '1':(1,0) }

with open(file,"r") as f:
    lines = [ line.split() for line in f.readlines() ]

perimeter_boundary = list()

y,x = (0,0)
perimeter = 0

for d,m,c in lines:

    dig_d = c[-2]
    distance = int(c[2:-2],16)
    perimeter = perimeter + distance

    y = y + ( directions[dig_d][0] * distance )

    x = x + ( directions[dig_d][1] * distance )

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
