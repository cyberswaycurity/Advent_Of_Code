with open("input.txt") as f:
    contents = f.readlines()

rotations = [c.strip('\n') for c in contents]

dial_start = 50

password = 0

for r in rotations:

    direction = r[0]
    number = int(r[1:])

    if direction == 'L':

        number = -1 * number

    if dial_start == 0 and number < 0:

        password -= 1

    dial_start = dial_start + number

    password += abs(dial_start // 100)

    if dial_start == 0:

        password += 1

    if dial_start % 100 == 0 and dial_start < 0:

        password += 1

    dial_start = dial_start % 100

print(password)
