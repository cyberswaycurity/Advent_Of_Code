from itertools import combinations

def min_pushes(indicator: list, buttons: list):

    for i in range(1,len(buttons)+1):

        for combos in combinations(buttons,i):

            check = 0
            for c in combos:

                check ^= c

                if check == int(indicator,2):

                    return i

with open("input.txt") as f:

    puzzle = f.readlines()

answer = 0

for line in puzzle:

    line = line.strip('\n').split()

    indicator = line[0]
    buttons = line[1:-1]
    indicator = indicator.strip('[]').replace('#','1').replace('.','0')

    new_buttons = []

    for b in buttons:

        toggled = ['0'] * len(indicator)
        locations = [int(n.strip()) for n in b[1:-1].split(',')]

        for i in locations:

            toggled[i] = '1'

        new_buttons.append(int(''.join(toggled),2))

    answer += min_pushes(indicator,new_buttons)

print(answer) 