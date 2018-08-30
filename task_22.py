#Task #22
#Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
#Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
#После чего опять просит угадать.
#И так пока пользователь не угадает выбранное число.

import random
pc_number = random.randint(1, 10)
print(pc_number)

user_number = 0
while user_number != pc_number:
    user_number = int(input('Enter a number:'))
    if user_number < pc_number:
        print('Enter bigger number')
    elif user_number > pc_number:
        print('Enter smaller number')
print('You have guessed')
