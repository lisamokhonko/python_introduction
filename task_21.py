#Task #21
#Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
#a) c использованием строк, b) без использования строк.

import random
number = random.randint(100000000000, 999999999999)
number = str(number)
print(number)

def get_max_digit_string(number): # returns int
	max_digit = 0
	for char in number:
		#print(char)
		if int(char) > max_digit:
			max_digit = int(char)
	return max_digit

print(get_max_digit_string(number))

def get_max_digit_int(number):
	number = int(number)
	max_digit = number % 10
	number = number // 10
	while number > 0:
		if number % 10 > max_digit:
			max_digit = number % 10
		number = number//10
	return max_digit

print(get_max_digit_int(number))