#import numpy as np

sqr = []
for _ in range(4):
    sqr.append([int(x) for x in input().split(' ')])

def get_cols(matrix):
    n = len(matrix[0])
    cols = [[] for _ in range(n)]

    for row in matrix:
        for col_i, val in enumerate(row):
            cols[col_i].append(val)

    return cols

acc = 0
magic = True
for d in ['r', 'c']:
    if d == 'c':
        matrix = get_cols(sqr)
    else:
        matrix = sqr
    i = 0
    while magic and i < 4:
        if i == 0:
            acc = sum(matrix[i])
            i += 1
        elif i < 4:
            if sum(matrix[i]) != acc:
                magic = False
            else:
                i += 1
                     
if magic:
    print("magic")
else:
    print("not magic")
