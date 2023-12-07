import sys

file = sys.argv[1]

with open(file,"r") as f:
    lines = [line.strip().split(': ') for line in f.readlines()]

lines = [ line[1].strip() for line in lines ]

lines = [ int(s.replace(' ','')) for s in lines ]

time,distance = lines

time_pressed = 0

no_beats = 0

while time_pressed < time:

    time_left = time - time_pressed

    speed = time_pressed

    races_dist = time_left * speed

    if races_dist > distance:

        break

    no_beats = no_beats + 1

    time_pressed = time_pressed + 1


time_pressed = time

while time_pressed > 0:

    time_left = time - time_pressed

    speed = time_pressed

    races_dist = time_left * speed

    if races_dist > distance:

        break

    no_beats = no_beats + 1

    time_pressed = time_pressed - 1

ways_to_beat = time - no_beats + 1

print(ways_to_beat)


