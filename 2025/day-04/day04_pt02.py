with open("input.txt") as f:

    grid = f.read().strip().split('\n')

grid = [list(c) for c in grid]

total_count = 0

continueRemoval = True

while True:

    removal_coords = []

    for y in range(len(grid)):

        for x in range(len(grid[0])):

            check = 0

            if grid[y][x] == '.':

                continue

            coordinates = [
                    (y,x-1),
                    (y,x+1),
                    (y-1,x),
                    (y+1,x),
                    (y-1,x+1),
                    (y-1,x-1),
                    (y+1,x+1),
                    (y+1,x-1)
                    ]

            for curr_y,curr_x in coordinates:

                if curr_y < 0 or curr_y >= len(grid):

                    continue

                if curr_x < 0 or curr_x >= len(grid[0]):

                    continue

                if grid[curr_y][curr_x] == '@':

                    check += 1

                if check > 3:

                    break


            if check < 4:

                removal_coords.append((y,x))

    if not removal_coords:

        break

    for y,x in removal_coords:

        grid[y][x] = '.'

    total_count += len(removal_coords)

print(total_count)





        
