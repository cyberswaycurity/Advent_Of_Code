with open("input.txt") as f:

    ranges = f.read()

ranges = ranges.split(',')

ranges = [ r.split('-') for r in ranges]

invalid_ids = []

for l,r in ranges:

    for i in range(int(l),int(r)+1):

        partitioning = len(str(i)) // 2

        if str(i)[0:partitioning] == str(i)[partitioning:]:

            invalid_ids.append(i)

print(sum(invalid_ids))
