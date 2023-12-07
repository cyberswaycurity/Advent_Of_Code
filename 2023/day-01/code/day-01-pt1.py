with open("../inputs/puzzle-input","r") as f:
    lines = f.readlines()

calibration_sum = 0

for line in lines:

    first_number = 0
    second_number = 0

    for i in line:
        if i.isdigit():
            first_number = int(i) * 10
            break

    for i in line[::-1]:
        if i.isdigit():
            second_number = int(i)
            break

    calibration_sum = calibration_sum + first_number + second_number

print("Calibration sum: ",calibration_sum)


