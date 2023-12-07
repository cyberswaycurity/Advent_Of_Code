import re

with open("../inputs/puzzle-input","r") as f:
    lines = [line.strip() for line in f.readlines()]

columns = len(lines[0])
rows = len(lines)

candidates = []

for idx,line in enumerate(lines):

    num_indexes = re.finditer(r"\d+",line)

    line_candidates = []

    for i in num_indexes:

        top_row = idx - 1
        bottom_row = idx + 1
        left_column = i.start() - 1
        right_column = i.end() + 1

        #CHECKS TOP ROW#
        if idx == 0:

            if left_column == -1:

                for j in lines[bottom_row][i.start():right_column]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if line[i.end()] != ".":

                    line_candidates.append(int(line[i.start():i.end()]))

            elif i.end() == columns:

                for j in lines[bottom_row][left_column:i.end()]:
                    
                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if line[left_column] != ".":

                    line_candidates.append(int(line[i.start():i.end()]))

            else: 

                for j in lines[bottom_row][left_column:right_column]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if line[i.end()] != "." or line[left_column] != ".":

                    line_candidates.append(int(line[i.start():i.end()]))


        #CHECKS BOTTOM ROW# 

        elif idx == (rows - 1): 

            if left_column == -1:

                for j in lines[top_row][left_column+1:right_column]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if line[i.end()] != ".":

                    line_candidates.append(int(line[i.start():i.end()]))

            elif i.end() == columns:

                for j in lines[top_row][left_column:i.end()]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if line[left_column] != ".":

                    line_candidates.append(int(line[i.start():i.end()]))

            else:

                for j in lines[top_row][left_column:right_column]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if line[i.end()] != "." or line[left_column] != ".":

                    line_candidates.append(int(line[i.start():i.end()]))

        #CHECKS ALL OTHER ROWS#
        else:

            if left_column == -1:

                for j in lines[top_row][i.start():right_column]:

                    if j!= ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                for j in lines[bottom_row][i.start():right_column]:

                    if j!= ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if line[i.end()] != ".":

                    line_candidates.append(int(line[i.start():i.end()]))

            elif i.end() == columns:

                for j in lines[top_row][left_column:i.end()]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                for j in lines[bottom_row][left_column:i.end()]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if lines[idx][left_column] != ".":

                    line_candidates.append(int(line[i.start():i.end()]))

            else:

                for j in lines[top_row][left_column:right_column]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                for j in lines[bottom_row][left_column:right_column]:

                    if j != ".":

                        line_candidates.append(int(line[i.start():i.end()]))
                        break

                if line[i.end()] != "." or line[left_column] != ".":

                        line_candidates.append(int(line[i.start():i.end()]))

    candidates.append(line_candidates)

solution = 0

for i in candidates:

    solution = solution + sum(i)

print(solution)
