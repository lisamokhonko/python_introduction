#Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к интервалу [-1;1],
# причем максимальное абсолютное значение элементов после нормирование должно быть равно 1.
# Например, последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]

import math

lst = [-5, 3, 10]

def normalize(lst): #-> list
    max_elem = abs(lst[0])
    for i in range(1, len(lst)):
        if abs(lst[i]) > max_elem:
            max_elem = lst[i]
        else:
            max_elem
    coeff = max_elem/1
    if lst[0] > 0:
        coeff
    else:
        coeff *= -1
    norm_matrix = []
    norm_matrix.append(lst[0]/coeff)
    for i in range(1, len(lst)):
        norm_matrix.append(lst[i]/coeff)
    return norm_matrix

print(normalize(lst))