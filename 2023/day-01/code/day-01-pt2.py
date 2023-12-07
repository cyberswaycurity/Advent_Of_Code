with open("../inputs/puzzle-input","r") as f:
    lines = f.readlines()

calibration_sum = 0

digit_letters = {"one":1, "two":2, "three":3, "four":4, "five": 5, "six":6, "seven":7, "eight":8, "nine":9}
digits = "0123456789"

for line in lines:

    candidates = []

    line = line.strip()
    for k,v in digit_letters.items():
        for i in range(0,len(line)):
            if line.startswith(k,i):
                candidate = (i,v)
                candidates.append(candidate)

    for idx,i in enumerate(line):
        if i in digits:
            candidate = (idx,int(i))
            candidates.append(candidate)

    candidates.sort()

    first_number = candidates[0][1] * 10
    second_number = candidates[-1][1]

    calibration_sum = calibration_sum + first_number + second_number

print("Calibration sum: ",calibration_sum)


