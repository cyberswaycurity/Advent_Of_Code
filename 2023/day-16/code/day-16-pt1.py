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

visited_nodes = list()

nodes = [(0,0,0,1)]

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


print(len(activated_nodes))
