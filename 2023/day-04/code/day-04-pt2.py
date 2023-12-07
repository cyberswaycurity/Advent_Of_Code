import sys

file = sys.argv[1]

with open(file,"r") as f:

    lines = [l.strip() for l in f.readlines()]

scratchcards_count = dict()

for idx,line in enumerate(lines):
    
    count = 0

    cards = 0

    card_number, scratchcard = line.split(": ")

    winning_numbers, numbers_to_check = scratchcard.split(" | ")

    winning_numbers = [int(i) for i in winning_numbers.split()]
    numbers_to_check = [int(i) for i in numbers_to_check.split()]

    if idx not in scratchcards_count.keys():

        scratchcards_count[idx] = 1

    else:

        scratchcards_count[idx] = scratchcards_count[idx] + 1

    for i in winning_numbers:

        if i in numbers_to_check:

            count = count + 1

    if count > 0:

        for i in range(idx+1,idx+count+1):

            if i >= len(lines):

                break

            if i in scratchcards_count.keys():

                scratchcards_count[i] = scratchcards_count[i] + scratchcards_count[idx]

            else:

                scratchcards_count[i] = scratchcards_count[idx]

print(sum(scratchcards_count.values()))
