import sys
from heapq import heappop,heappush

file = sys.argv[1]

with open(file,"r") as f:

    city_blocks = [ [ int(i) for i in line.strip('\n') ] for line in f.readlines() ]

directions = [ (0,1), (0,-1), (1,0), (-1,0) ]

beg_block = (0,0)
end_block = (len(city_blocks) - 1, len(city_blocks[0]) - 1)

# (heat_loss, (y,x), (dy,dx), step_count)

heap = [ (0,(0,0),(1,0),0),(0,(0,0),(0,1),0)]
visited = set()

while heap:

    node = heappop(heap)
    heat_loss,block,direction,step_count = node

    if block == end_block:

        print(heat_loss)

        break

    if (block,direction,step_count) in visited:

        continue

    y,x = block
    dy,dx = direction

    for y1,x1 in directions:

        new_y = y + y1
        new_x = x + x1

        nxt_block = (new_y,new_x)

        if (y1 == -dy) and (x1 == -dx):

            continue

        if  new_y < 0 or new_y >= len(city_blocks)  or new_x < 0  or new_x >= len(city_blocks[0]):

            continue

        if step_count >= 10 and ( dy == y1 and dx == x1):

            continue

        if step_count < 10 and ( dy == y1 and dx == x1 ):

            new_node =  ( heat_loss + city_blocks[new_y][new_x],nxt_block,(y1,x1),step_count + 1)
            heappush(heap,new_node)
            continue

        if step_count >= 4:

            new_node =  ( heat_loss + city_blocks[new_y][new_x],nxt_block,(y1,x1),1)
            heappush(heap,new_node)

    visited.add((block,direction,step_count))
