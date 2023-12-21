import sys

file = sys.argv[1]

with open(file,"r") as f:

    lines = [ [ c for c in line.strip() ] for line in f.readlines() ]

rows = len(lines)

while rows > 0:

    for i in range(0,len(lines) - 1):

        for idx,(n,s) in enumerate(zip(lines[i],lines[i+1])):

            if n == '.' and s == 'O':

                lines[i][idx] = 'O'
                lines[i + 1][idx] = '.'

    rows = rows - 1
    
load = 0

rows = len(lines)

for line in lines:

    load = load + ( line.count('O') * rows )

    rows = rows - 1

print(load)
