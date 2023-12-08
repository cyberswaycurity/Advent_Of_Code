import sys

file = sys.argv[1]

with open(file,"r") as f:

    lines = [line.strip() for line in f.readlines()]

moves = lines[0]
nodes = [ i.split(' = ') for i in lines[2:]]

nodes_map = dict()
directions_map = {'L':0 , 'R':1}
for i in nodes:

    key = i[0]
    value = tuple(i[1].replace("(",'').replace(")",'').split(", "))

    nodes_map[key] = value

starting_key = 'AAA'
step_count = 0

while starting_key != 'ZZZ':

    for c in moves:

        idx = directions_map[c]
        starting_key = nodes_map[starting_key][idx]
        step_count = step_count + 1

        if starting_key == 'ZZZ':

            break

print(step_count)
