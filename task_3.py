#Task #3
#Найти результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c % 4 + b

a = 20
b = 30
c = 1
abc_result = (a + b)/12*c%4 + b

print('Result of (a + b)/12*c%4 + b','for a = %.2f, b = %.2f, c = %.2f is %.5f'
      %(a, b, c, abc_result))
