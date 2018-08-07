#Task #5
#Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)**3 - cos( c )

import math
a = 10
b = -10
c = 15
#ab_sum = a + b
if a + b != 0:
    abc_result = math.fabs(a - b)/math.pow(a + b, 3) - math.cos(c)
    print('Result of |a - b| /(a + b)**3 - cos(c) for a = %.2f, b = %.2f, c = %.2f is %.5f'
          %(a, b, c, abc_result))
else: print('Error: Division by zero, sum of a = %.2f and b = %.2f is 0' %(a, b))