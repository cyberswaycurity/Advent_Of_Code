import sys
from time import sleep

file = sys.argv[1]

with open(file,"r") as f:

    lines = [ [ int(i) for i in line.strip().split() ] for line in f.readlines() ]

final_analysis_sum = 0

for i in lines:

    history = [ n for n in i ]

    predictions = [history]

    notZero = True

    beg_idx = 0

    while notZero:

        predictions_step = []

        for i in range(len(predictions[beg_idx]) - 1):

            if not any(predictions[beg_idx]):

                notZero = False

                predictions.pop()

                break

            diff = predictions[beg_idx][i + 1] - predictions[beg_idx][i] 

            predictions_step.append(diff)

        beg_idx = beg_idx + 1

        if notZero:

            predictions.append(predictions_step)

    prediction_next_value = 0

    while predictions:

        results = predictions.pop()

        x = results[-1]

        prediction_next_value = x + prediction_next_value

    final_analysis_sum = final_analysis_sum + prediction_next_value

print(final_analysis_sum)
