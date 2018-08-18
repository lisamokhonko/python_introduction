#Task #13
#Написать функцию, которая вычислит площадь и объем конуса по его радиусу и высоте.
#Результат работы функции должен вернуть два значения.

import math
def cone_square_and_volume(radius, height): # returns 2 floats
    l = math.sqrt(pow(radius, 2) + pow(height, 2))
    square = math.pi*radius*l + math.pi*pow(radius, 2)
    volume = height/3*math.pi*pow(radius, 2)
    return square, volume
