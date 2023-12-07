import sys
import re

file = sys.argv[1]

with open(file,"r") as f:

    file = f.read().strip()

sections = re.split(r"[a-z-\s]+:",file)
sections = [i.strip() for i in sections[1:]]

seeds = [ int(i) for i in sections[0].strip().split()]

maps = sections[1:]
maps = [ [ j.split() for j in i.split('\n')] for i in maps]


locations = []

for i in seeds:

    key = i

    for m in maps:

        for i in m:

            if key >= int(i[1]) and key <= (int(i[1]) + int(i[-1])):

                key = int(i[0]) + (key - int(i[1]))

                break

    locations.append(key)

print(min(locations))
