#Task #23
#Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную,
#на первый взгляд, награду: столько пшеничных зёрен, сколько окажется на шахматной доске,
#если на первую клетку положить одно зерно, на вторую — два зерна,
#на третью — четыре зерна и т. д. Оказалось, что такого количества зерна нет на всей планете
#(# оно равно 2**64 − 1 зерен). Посчитайте, начиная с какой клетки по счету,
#общее количество зерен, которое должен был бы отдать раджа изобретателю
#было больше 1 000 000 зерен и сколько конкретно зерен он должен был бы отдать.

import math

def chess_reward(): # returns 2 ints (cell number and total number of corns)
    start_number = 1
    start_cell = 1
    q = 2
    current_number = start_number
    current_cell = start_cell
    while current_number < 1000000:
        #if current_number < 1000000:
            current_number = current_number + pow(2, current_cell)
            current_cell += 1
        #else:
         #   break
    return current_cell, current_number

print(chess_reward())
