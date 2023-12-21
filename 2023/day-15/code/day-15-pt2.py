import sys

def hash(letters):

    current_value = 0

    for c in letters:

        current_value = current_value + ord(c)
        current_value = current_value * 17
        current_value = current_value % 256

    return current_value
        
file = sys.argv[1]

with open(file,"r") as f:

    steps = f.read().strip().split(',')

boxes = [ [] for i in range(0,256) ]

lens_labels = [ [] for i in range(0,256) ]

for step in steps:

    if ( step[-1] == '-' ) and ( step[:-1] in lens_labels[hash(step[:-1])] ):

        idx = lens_labels[hash(step[:-1])].index(step[:-1])
        boxes[hash(step[:-1])].pop(idx)
        lens_labels[hash(step[:-1])].pop(idx)

        continue

    elif step[-1] == '-':

        continue

    lens_label = step[:-2]
    focal_length = int(step[-1])
    box = hash(lens_label)

    if lens_label in lens_labels[box]:

        idx = lens_labels[box].index(lens_label)
        boxes[box][idx] = focal_length
        
        continue

    lens_labels[box].append(lens_label)
    boxes[box].append(focal_length)

solution = 0

for idx,box in enumerate(boxes):
    
    if box:

        for slot,f in enumerate(box):

            solution = solution + ( (idx + 1) * (slot+1) * f )

print(solution)
