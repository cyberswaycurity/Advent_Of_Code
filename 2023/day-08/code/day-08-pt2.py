import sys
from math import lcm

file = sys.argv[1]

with open(file,"r") as f:

    lines = [line.strip() for line in f.readlines()]

moves = lines[0]
nodes = [ i.split(' = ') for i in lines[2:]]

nodes_map = dict()
directions_map = {'L':0 , 'R':1}

starting_keys = []

for i in nodes:

    key = i[0]
    value = tuple(i[1].replace("(",'').replace(")",'').split(", "))
    nodes_map[key] = value

    if key[-1] == 'A':

        starting_keys.append(key)

z_check = [ 0 for i in range(len(starting_keys)) ]

step_count = 0

notAllZ = True

while notAllZ:

    for c in moves:

        step_count = step_count + 1

        for idx,n in enumerate(starting_keys):

            tup_idx = directions_map[c]
            starting_keys[idx] = nodes_map[n][tup_idx]
            
            if starting_keys[idx][-1] == 'Z' and z_check[idx] == 0:

                z_check[idx] = step_count

            if 0 not in z_check:

                notAllZ = False

                break

print(lcm(*z_check))
