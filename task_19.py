#Task #19
#Написать функцию для поиска разницы между максимальным и минимальным числом среди num_limit
#случайно сгенерированных чисел в указанном числовом диапазоне.

import random

def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    num_min = random.randint(lower_bound, upper_bound)
    num_max = 0
    result = 0
    current_value = 0
    for i in range(num_limit):
        current_value = random.randint(lower_bound, upper_bound)
        if num_min >= current_value:
            num_min = current_value
        if num_max <= current_value:
            num_max = current_value
        print(current_value)
    result = num_max - num_min
    return result

print('Difference is:',diff_min_max(5, 1, 10))