import sys
from queue import Queue

file = sys.argv[1]

with open(file,"r") as f:

    lines = [line.strip() for line in f.readlines()]

'''
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''

pipe_directions = { 
                'S':[(0,1),(0,-1),(1,0),(-1,0)],
                '|':[(-1,0),(1,0)],
                '-':[(0,1),(0,-1)],
                'L':[(-1,0),(0,1)],
                'J':[(-1,0),(0,-1)],
                '7':[(1,0),(0,-1)],
                'F':[(1,0),(0,1)]
                }

pipes_per_direction = {

    (-1,0):['|','7','F','S'],
    (1,0):['|','L','J','S'],
    (0,1):['-','7','J','S'],
    (0,-1):['-','L','F','S']

    }

start_point = list()

for y in range(len(lines)):

    for x in range(len(lines[y])):

        if lines[y][x] == 'S':

            start_point = [ y , x , 0 , 'S']

            break

    if start_point:

        break

farthest_point = 0

visited_nodes = []

nodes_queue = Queue()
nodes_queue.put(start_point)

visits = 0
while not nodes_queue.empty():

    y,x,steps,pipe = nodes_queue.get()

    visits = visits + 1

    new_step_count = steps + 1

    if steps > farthest_point:

        farthest_point = steps

    for dirct in pipe_directions[pipe]:

        y1,x1 = dirct

        y_new = y + y1
        x_new = x + x1

        if (y_new == -1 or y_new == len(lines)) or (x_new == -1 or x_new == len(lines[0])):

            continue

        nxt_pipe = lines[y_new][x_new]

        child_node = (y_new,x_new)

        if child_node in visited_nodes:

            continue

        if nxt_pipe == '.':

            continue
        
        if nxt_pipe not in pipes_per_direction[dirct]:

            continue

        pipe_to_queue = [ y_new, x_new, new_step_count, nxt_pipe ]

        nodes_queue.put(pipe_to_queue)

    curr_node = (y,x)
    visited_nodes.append(curr_node)

print(visits)
print(farthest_point)
