#Task #12
#Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного пользователем в консоли,
# без использования операторов цикла. a) cо строками, б) без использования строк.

def sum_string(number_value):
    sum_value = int(number_value[0]) + int(number_value[1]) + int(number_value[2])
    return sum_value

def sum_digit(number_value):
    number_value = int(number_value)
    digit1 = number_value//100
    digit2 = (number_value - digit1*100)//10
    digit3 = (number_value - digit1*100 - digit2*10)
    sum_value = digit1 + digit2 + digit3
    return sum_value

number_value = input('Enter a number: ')
if len(number_value) == 3:
    calculation_way = input('Select calculation way, 1 - as String, 2 - as Number: ')
    if calculation_way in ('1', '2'):
        if calculation_way == 1:
            sum_value = sum_string(number_value)
        else:
            sum_value = sum_digit(number_value)
        print('Sum of three digits is', sum_value)
    else:
        print('Error: Select correct calculation way')
else:
    print('Error: Length of entered number does not equal to 3 digits')