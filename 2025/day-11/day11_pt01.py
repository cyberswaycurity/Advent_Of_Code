with open("input.txt") as f:
    puzzle = f.readlines()

devices = dict()

for p in puzzle:

    p = p.strip()

    k, v = p.split(':')

    k = k.strip()
    v = v.strip().split()

    devices[k] = v

stack = ['you']

answer = 0

while stack:

    current = stack.pop()

    if current == 'you' and stack:

        continue

    if current == 'out':

        answer += 1
        continue

    stack.extend(devices[current])

print(answer)