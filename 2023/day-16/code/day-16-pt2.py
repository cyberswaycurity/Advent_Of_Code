import sys

file = sys.argv[1]

with open(file,"r") as f:

    spaces = [line.strip() for line in f.readlines() ]

beam_dir = {
        (0,1):{ '|':[(-1,0),(1,0)], '.':[(0,1)], '-':[(0,1)], '/':[(-1,0)], '\\':[(1,0)] },
        (0,-1):{ '|':[(-1,0),(1,0)], '.':[(0,-1)], '-':[(0,-1)], '/':[(1,0)], '\\':[(-1,0)] },
        (1,0):{ '|':[(1,0)], '.':[(1,0)], '-':[(0,1),(0,-1)], '/':[(0,-1)], '\\':[(0,1)] },
        (-1,0):{ '|':[(-1,0)], '.':[(-1,0)], '-':[(0,1),(0,-1)], '/':[(0,1)], '\\':[(0,-1)] },
        }


edge_headings = list()

for y in range(len(spaces)):

    edge_headings.append((y,0,0,1))
    edge_headings.append((y,len(spaces[0]) - 1,0,-1))

for x in range(len(spaces[0])):

    edge_headings.append((0,x,1,0))
    edge_headings.append((len(spaces) - 1,x,-1,0))

maximum_energy = 0

while edge_headings:

    visited_nodes = list()

    starting_node = edge_headings.pop()
    nodes = [starting_node]

    activated_nodes = []

    while nodes:

        curr_node = nodes.pop()

        y,x,y1,x1 = curr_node

        activated_node = (y,x)

        if (curr_node in visited_nodes) or ( y < 0 ) or (y >= len(spaces)) or (x < 0) or (x >= len(spaces[0])):
            continue

        if activated_node not in activated_nodes:

            activated_nodes.append(activated_node)

        curr_char = spaces[y][x]
        curr_dir = (y1,x1)

        for i in beam_dir[curr_dir][curr_char]:

            y2,x2 = i    
            new_node = (y+y2,x+x2,y2,x2)
            nodes.append(new_node)

        visited_nodes.append(curr_node)

    energy = len(activated_nodes)

    if maximum_energy < energy :

        maximum_energy = energy

print(maximum_energy)
