import sys

file = sys.argv[1]

with open(file,"r") as f:

    steps = f.read().strip().split(',')

final_value = 0

for step in steps:

    current_value = 0

    for c in step:

        current_value = current_value + ord(c)
        current_value = current_value * 17
        current_value = current_value % 256

    final_value = final_value + current_value

print(final_value)
