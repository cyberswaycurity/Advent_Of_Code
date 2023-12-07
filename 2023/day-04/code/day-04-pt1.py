import sys

file = sys.argv[1]

with open(file,"r") as f:

    lines = [l.strip() for l in f.readlines()]

scratchcards_value = 0

for line in lines:
    
    count = 0

    card_number, scratchcard = line.split(": ")

    winning_numbers, numbers_to_check = scratchcard.split(" | ")

    winning_numbers = [int(i) for i in winning_numbers.split()]
    numbers_to_check = [int(i) for i in numbers_to_check.split()]

    for i in winning_numbers:

        if i in numbers_to_check:

            count = count + 1

    if count != 0:

        scratchcards_value = scratchcards_value + 2**(count - 1)


print(scratchcards_value)

