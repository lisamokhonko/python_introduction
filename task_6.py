#Task #6
#Найти результат выражения для произвольных значений a,b,c: (ln(1 + c) / -b)**4 + |a|

import math
a = 10
b = 1
c = 25
if b != 0:
    abc_result = pow(math.log1p(1 + c)/(-b), 4) + math.fabs(a)
    print('Result of (ln(1 + c) / -b)**4 + |a| for a = %.2f, b = %.2f, c = %2.f is %.5f'
    %(a, b, c, abc_result))
else:
    print('Error: division by zero, b = 0')