#Test #5
#Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем. Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.

def nearest_number(number_1, number_2):
    #if number_1.lstrip('-').replace('.','',1).isdigit() and number_2.lstrip('-').replace('.','',1).isdigit():
    numbers = [number_1, number_2]
    numbers.sort(key=lambda elem: abs(10 - elem))
    return numbers[0]


number_1 = int(input('Enter first number:'))
number_2 = int(input('Enter second number:'))
print(nearest_number(number_1, number_2))