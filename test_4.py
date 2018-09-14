#Test #4
#Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры

def multiply_result(user_number):
    result = 1
    user_number = str(user_number)
    for char in user_number:
        if int(char) % 2 != 0:
            result *= int(char)
    return result

user_number = input('Enter a number:')
print(multiply_result(user_number))