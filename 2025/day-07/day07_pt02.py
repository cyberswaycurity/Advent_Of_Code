from collections import defaultdict

with open("input.txt") as f:

    puzzle = f.read().split('\n')[:-1]

puzzle = [[c for c in p] for p in puzzle]

first_r = puzzle[0]
space = puzzle[1:]

beams = defaultdict(int)

for i,b in enumerate(first_r):

    if b == 'S':

        beams[i] = 1

for s in space:

    splits = defaultdict(int)

    for b in beams:

        if s[b] == '^':

            if s[b - 1] == '.' and s[b + 1] == '.':

                splits[b-1] += beams[b]
                splits[b+1] += beams[b]

            elif s[b-1] == '.':

                splits[b-1] += beams[b]

            else:
                splits[b+1] += beams[b]

        else:
            splits[b] += beams[b]

    beams = splits

print(sum(beams.values()))
