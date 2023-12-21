import sys

file = sys.argv[1]

with open(file,"r") as f:

    lines = [ [ c for c in line.strip() ] for line in f.readlines() ]

rows = len(lines)

cycles = 1000000000

cycles_count = 0

loads = [lines]

while cycles_count < cycles :

    while rows > 0:

        for i in range(0,len(lines) - 1):

            for idx,(n,s) in enumerate(zip(lines[i],lines[i+1])):

                if n == '.' and s == 'O':

                    lines[i][idx] = 'O'
                    lines[i + 1][idx] = '.'

        rows = rows - 1
        
    #WEST
    transposed = list(map(list,zip(*lines)))
    lines = transposed

    rows = len(lines)

    while rows > 0:

        for i in range(0,len(lines) - 1):

            for idx,(n,s) in enumerate(zip(lines[i],lines[i+1])):

                if n == '.' and s == 'O':

                    lines[i][idx] = 'O'
                    lines[i + 1][idx] = '.'

        rows = rows - 1

    #SOUTH
    transposed = list(map(list,zip(*lines)))
    lines = transposed[::-1]

    rows = len(lines)

    while rows > 0:

        for i in range(0,len(lines) - 1):

            for idx,(n,s) in enumerate(zip(lines[i],lines[i+1])):

                if n == '.' and s == 'O':

                    lines[i][idx] = 'O'
                    lines[i + 1][idx] = '.'

        rows = rows - 1

    #EAST

    transposed = list(map(list,zip(*lines)))
    lines = transposed[::-1]

    rows = len(lines)

    while rows > 0:

        for i in range(0,len(lines) - 1):

            for idx,(n,s) in enumerate(zip(lines[i],lines[i+1])):

                if n == '.' and s == 'O':

                    lines[i][idx] = 'O'
                    lines[i + 1][idx] = '.'

        rows = rows - 1

    lines = lines[::-1]
    transposed = list(map(list,zip(*lines)))
    lines = transposed[::-1]

    cycles_count = cycles_count + 1

    rows = len(lines)

    load = tuple(tuple(i) for i in lines)

    if load in loads:

        break

    loads.append(load)
   
repeat = tuple(tuple(i) for i in lines)

cycle_start = loads.index(repeat)

cycle_interval = cycles_count - cycle_start

final_index = ((cycles - cycle_start) % cycle_interval) + cycle_start

load_sum = 0

rows = len(loads[final_index])

for i in loads[final_index]:

    load_sum = load_sum + ( i.count('O')*rows ) 
    rows = rows - 1

print(load_sum)
