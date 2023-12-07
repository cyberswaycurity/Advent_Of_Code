import sys

file = sys.argv[1]

with open(file,"r") as f:
    lines = [line.strip().split(': ') for line in f.readlines()]

lines = [ x[1].strip() for x in lines ]

lines = [ [int(i) for i in line.split() ] for line in lines]

print(lines)

races = len(lines[0])

times = lines[0]
distance = lines[1]

record_breaks = []

for r in range(0,races):

    beats = []

    dist_to_beat = distance[r]

    time_allowed = times[r]

    time_pressed = 1

    while time_pressed < time_allowed:

        time_left = time_allowed - time_pressed
        speed = time_pressed

        dist = time_left * speed

        if dist > dist_to_beat:

            beats.append(dist)

        time_pressed = time_pressed + 1

    record_breaks.append(beats)

solution = 1

for breaks in record_breaks:

    solution = solution * len(breaks) 

print(solution)

