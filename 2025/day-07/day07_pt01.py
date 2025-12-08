with open("input.txt") as f:

    puzzle = f.read().split('\n')[:-1]

puzzle = [[c for c in p] for p in puzzle]

first_r = puzzle[0]
space = puzzle[1:]

beams = set()

for i,b in enumerate(first_r):

    if b == 'S':

        beams.add(i)

solution = 0

for s in space:

    splits = set()

    for b in beams:

        if s[b] == '^':

            if s[b - 1] == '.' and s[b + 1] == '.':

                solution += 1

                splits.add(b-1)
                splits.add(b+1)

            elif s[b-1] == '.':

                splits.add(b-1)

            else:
                splits.add(b+1)

        else:
            splits.add(b)

    beams = splits

print(solution)


