#Task #2
#Найти результат выражения для произвольных значений a,b: (a2 + b2) % 2

import math
a = 3
b = 6
ab_result = (pow(a, 2) + pow(b, 2))%2

#Need to know how to put % sign in such string
print('Result of (a**2 + b**2)%2', 'for a = %.2f and b = %.2f is %d'
      %(a, b, ab_result))