with open("input.txt") as f:

    ranges = f.read()

ranges = ranges.split(',')

ranges = [ r.split('-') for r in ranges]

invalid_ids = []

for l,r in ranges:

    for i in range(int(l),int(r)+1):

        curr_len = len(str(i))

        for j in range(1,curr_len):

            if curr_len % j != 0:

                continue

            temp_list = []

            for k in range(0,curr_len,j):

                temp_list.append(str(i)[k:k+j])

            if len(set(temp_list)) == 1:

                invalid_ids.append(i)

                break

print(sum(invalid_ids))
