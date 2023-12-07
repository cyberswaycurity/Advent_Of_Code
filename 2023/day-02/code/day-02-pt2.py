with open("../inputs/puzzle-input","r") as f:
    lines = f.readlines()

lines = [line.strip().split(": ")[1] for line in lines]

cube_sets = [line.split("; ") for line in lines]

cube_sets = [[i.split(", ") for i in cube_set] for cube_set in cube_sets]

sum_of_powers = 0

for idx,cube_set in enumerate(cube_sets):

    colors = {"red":0, "green":0, "blue":0}

    for cubes in cube_set:

        for i in cubes:

            count_color = i.split()

            if int(count_color[0]) > colors[count_color[1]]:

                colors[count_color[1]] = int(count_color[0])

    sum_of_powers = sum_of_powers + (colors["red"] * colors["green"] * colors["blue"])


print("sum of powers: ",sum_of_powers)
