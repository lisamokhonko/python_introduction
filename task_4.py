#Task #4
#Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c

a = 10
b = 10
c = 20
ab_sum = a + b
if ab_sum != 0:
    abc_result = (a - b*c)/(a + b)%c
    print('Result of (a - b * c ) / ( a + b ) % c', 'for a = %.2f, b = %.2f, c = %.2f is %.5f' %(a, b, c, abc_result))
else: print('Error: Division by zero. Sum of a = %.2f and b = %.2f is 0' %(a, b))
