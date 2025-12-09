from itertools import combinations
from math import sqrt
import heapq
from math import prod
from collections import Counter

def find(x):

    if parent[x] == x:

        return x

    return find(parent[x])

def union(x,y):

    parent_x = find(x)
    parent_y = find(y)
    
    if parent_x == parent_y:

        return False

    if rank[parent_x] < rank[parent_y]:

        parent_x, parent_y = parent_y, parent_x

    parent[parent_y] = parent_x

    if rank[parent_x] == rank[parent_y]:
        rank[parent_x] += 1

    return True



with open("input.txt") as f:

    puzzle = f.read().split('\n')[:-1]


puzzle = [tuple(map(int,p.split(','))) for p in puzzle]

pairs = list(combinations(puzzle,2))

parent = {p: p for p in puzzle}
rank = {p: 0 for p in puzzle}

min_heap = []
heapq.heapify(min_heap)

for p in pairs:

    (x1,y1,z1),(x2,y2,z2) = p

    distance = sqrt(pow((x2-x1),2) + pow((y2-y1),2) + pow((z2-z1),2))

    heapq.heappush(min_heap,(distance,(p[0],p[1])))

circuits = []

connections_made = 0

while True:

    dist,(x,y) = heapq.heappop(min_heap)

    if union(x,y):

        if len(set(find(node) for node in puzzle)) == 1:

            print(x[0] * y[0])
            break
