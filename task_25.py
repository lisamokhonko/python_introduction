#Task #25
#Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию,
#которая переставляет его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
#Примечание: использовать метод random.shuffle не допускается.
import random

list_to_shuffle = [1]
for i in range(3, 100, 2):
    list_to_shuffle = list_to_shuffle + [i]
print(list_to_shuffle, type(list_to_shuffle), len(list_to_shuffle))


def shuffle_list(list_to_shuffle):
    original_list = list_to_shuffle.copy()
    length = len(original_list)
    for i in range(length):
        index = random.randint(0, length - 1)
        list_to_shuffle[i] = original_list[index]
    return list_to_shuffle

shuffle_list(list_to_shuffle)
print(list_to_shuffle)