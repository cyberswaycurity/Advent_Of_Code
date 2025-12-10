from collections import defaultdict

with open("08_puzzle_input") as f:

    puzzle = f.read().split('\n')[:-1]

puzzle = [ list(p.strip().split(' | ')) for p in puzzle]

interim = []

for s,d in puzzle:

    interim.append([sorted(s.split(),key=len),d.split()])

puzzle = interim

answer = 0

for s,d in puzzle:

    segments = s
    digits = d

    digits_map = dict()

    digits_map['1'] = set(segments[0])
    digits_map['7'] = set(segments[1])
    digits_map['4'] = set(segments[2])
    digits_map['8'] = set(segments[-1])

    five_segs = segments[3:6]
    six_segs = segments[6:-1]

    for s in six_segs:

        if len(set(s) - digits_map['4']) == 2:

            digits_map['9'] = set(s)

            six_segs.remove(s)

            break

    for s in six_segs:

        if len(set(s) - digits_map['1']) == 4:

            digits_map['0'] = set(s)
            six_segs.remove(s)

            break

    digits_map['6'] = set(six_segs.pop())

    for s in five_segs:

        if len(set(s) - digits_map['7']) == 2:
            digits_map['3'] = set(s)
            five_segs.remove(s)
            break

    for s in five_segs:

        if len(set(s) - digits_map['4']) == 2:
            digits_map['5'] = set(s)
            five_segs.remove(s)
            break

    digits_map['2'] = set(five_segs.pop())

    number = ''

    for d in digits:

        for k,v in digits_map.items():

            if set(d) == v:

                number = number + k
                break

    answer += int(number)

print(answer)
