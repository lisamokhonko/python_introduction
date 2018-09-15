#Test #8
#В одномерном списке поменять местами минимальный и максимальный элементы.
# Остальные оставить на своих местах. *IN PLACE*

lst = [3, 8, 7, 5, 9, 6, 2, 6, 7]

def swap_min_max(lst): #-> list
    max = lst[0]
    min = lst[0]
    max_idx = 0
    min_idx = 0
    for i in range(1, len(lst)):
        if max < lst[i]:
            max = lst[i]
            max_idx = i
        if min > lst[i]:
            min = lst[i]
            min_idx = i
    lst[max_idx] = min
    lst[min_idx] = max
    return lst

print(swap_min_max(lst))