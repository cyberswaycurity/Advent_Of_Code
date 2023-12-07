valid_cube_configuration = {"red":12, "green":13, "blue":14}

with open("../inputs/puzzle-input","r") as f:
    lines = f.readlines()

lines = [line.strip().split(": ")[1] for line in lines]

cube_sets = [line.split("; ") for line in lines]

cube_sets = [[i.split(", ") for i in cube_set] for cube_set in cube_sets]

sum_of_IDs = 0

for idx,cube_set in enumerate(cube_sets):

    isPossible = True

    for cubes in cube_set:

        for i in cubes:

            count_color = i.split()

            if int(count_color[0]) > valid_cube_configuration[count_color[1]]:

                isPossible = False
                break

        if not isPossible:

            break

    if isPossible:

        sum_of_IDs = sum_of_IDs + (idx + 1)

print("sum of IDs: ",sum_of_IDs)




    
