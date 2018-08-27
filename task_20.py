#Task #20
#Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди num_limit
#случайно сгенерированных чисел в указанном числовом диапазоне.
#Т.е. от суммы четных чисел вычесть сумму нечетных чисел.

import random
def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
    sum_even = 0
    sum_odd = 0
    current_value = 0
    result = 0
    for i in range(num_limit):
        current_value = random.randint(lower_bound, upper_bound)
        #print(current_value)
        if current_value % 2 == 0:
            sum_even += current_value
        else:
            sum_odd += current_value
    result = sum_even - sum_odd
    #print(result)
    return result

diff_even_odd(5, 0, 10)
