def max_search(bank,bank_len):

    max_idx = 0

    max_num = bank[max_idx]

    for i in range(max_idx+1,len(bank)):

        if int(bank[i]) > int(max_num):
            max_idx = i
            max_num = bank[i]


    return max_idx,max_num

with open("input.txt") as f:

    banks = f.readlines()

banks = [b.strip() for b in banks]

jolts = list()

for b in banks:

    max_idx,max_num = max_search(b,len(b))

    if max_idx == 0:

        _,next_num = max_search(b[1:],len(b[1:]))

        jolts.append(int(max_num + next_num))

    elif max_idx == len(b) - 1:

        sub_b = b[0:max_idx]

        _,next_num = max_search(b[0:max_idx],max_idx)

        jolts.append(int(next_num + max_num))

    else:

        _,left_num = max_search(b[0:max_idx],len(b[0:max_idx]))
        _,right_num = max_search(b[max_idx+1:],len(b[max_idx+1:]))

        left_candidate = left_num + max_num
        right_candidate = max_num + right_num

        if int(left_candidate) > int(right_candidate):

            jolts.append(int(left_candidate))

        else:

            jolts.append(int(right_candidate))

print(sum(jolts))
