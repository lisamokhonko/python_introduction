#Test #11
#В двумерном списке (матрица=список списков) отсортировать четные столбцы по возрастанию, а нечетные - по убыванию

import pprint
import numpy as np
matrix = [[3, 8, 7], [5, 9, 6], [2, 6, 7]]


def sort_alt(matrix): #-> matrix
    array = np.array(matrix)
    tr = array.transpose()
    #pprint.pprint(tr)
    for i in range( len(matrix)):
        if (i % 2 == 0):
            tr[i].sort()
        else:
            tr[i] = -tr[i]
            tr[i].sort()
            tr[i] = -tr[i]
    array = tr.transpose()
    return array

print(sort_alt(matrix))