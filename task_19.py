#Task #19
#Написать функцию для поиска разницы между максимальным и минимальным числом среди num_limit
#случайно сгенерированных чисел в указанном числовом диапазоне.

import random

def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    result = 0
    for i in range(num_limit):
        if i != 0:
            current_value = random.randint(lower_bound, upper_bound)
            print(current_value)
            if num_min > current_value:
                num_min = current_value
            if num_max < current_value:
                num_max = current_value
        elif i == 0:
            current_value = random.randint(lower_bound, upper_bound)
            print('First value', current_value)
            num_min = current_value
            num_max = current_value
    print(num_min, num_max)
    result = num_max - num_min
    return result

print('Difference is:',diff_min_max(10, 100, 200))

print('Difference is:',diff_min_max(10, -200, -100))

#print(random.randint(-200, -100))