#Task #18
#Каждому символу в таблице символов Unicode соответствует число.
#Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам,
#стоящим между двумя заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’.
#Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.

def sum_symbol_codes(first, last): # returns int
    result = 0
    first_num = ord(first)
    last_num = ord(last) + 1
    if first_num <= last_num:
        for i in range(first_num, last_num):
            result += i
    return result

print(sum_symbol_codes('b', 'a'))
