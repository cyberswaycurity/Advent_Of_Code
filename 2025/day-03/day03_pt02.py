with open("input.txt") as f:

    banks = f.readlines()

banks = [b.strip() for b in banks]

jolts = list()

for b in banks:

    b = [int(c) for c in b]

    jolt = 0

    for i in range(-11,1,1):

        if i == 0:

            i = None

        digit = max(b[:i])

        jolt = (jolt * 10) + digit

        beg_idx = b[:i].index(digit) + 1

        b = b[beg_idx:]

    jolts.append(jolt)

print(sum(jolts))





        


