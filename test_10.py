#Test #10
#Для заданной матрицы (3*3) найти все ее седловые точки и вернуть список их координат (список списков).
# Седловых точек может не быть, может быть 1 и более.

import numpy as np

matrix = [[3, 8, 7], [5, 9, 6], [2, 6, 7]]

def find_saddle_points(matrix): #-> list of lists
    rowmins = []
    rowmaxs = []
    colmins = []
    colmaxs = []

    for i, row in enumerate(matrix):
        min_r = min(row)
        max_r = max(row)
        for j, x in enumerate(row):
            if x == min_r:
                rowmins.append((i, j))
            if x == max_r:
                rowmaxs.append((i, j))

    t = [list(column) for column in zip(*matrix)]  # transpose of matrix

    for j, col in enumerate(t):
        min_c = min(col)
        max_c = max(col)
        for i, x in enumerate(col):
            if x == min_c:
                colmins.append((i, j))
            if x == max_c:
                colmaxs.append((i, j))
    saddle_points = list((set(rowmins) & set(colmaxs)) | (set(rowmaxs) & set(colmins)))
    saddle_points_list = [list(i) for i in saddle_points]

    return saddle_points_list

print(find_saddle_points(matrix))