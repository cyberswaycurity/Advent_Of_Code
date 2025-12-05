with open("input.txt") as f:

    puzzle = f.read().strip().split('\n\n')

id_ranges, ids = puzzle

id_ranges = [ list(map(int,n.split('-'))) for n in id_ranges.split('\n')]
ids = [ int(i) for i in ids.split('\n')]

id_ranges = sorted(id_ranges)

consolidated_ranges = [id_ranges[0]]

for i in range(1,len(id_ranges)):

    if id_ranges[i][0] <= consolidated_ranges[-1][1]:

        consolidated_ranges[-1][1] = max(consolidated_ranges[-1][1],id_ranges[i][1])

    else:

        consolidated_ranges.append(id_ranges[i])


solution = 0

for b,e in consolidated_ranges:

    solution += (e - b + 1)

print(solution)
