#Task #17
#Написать функцию решения квадратного уравнения.

import math

def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots, 1 root and None or 2 Nones
    d = pow(b, 2) - 4*a*c
    if d > 0:
        return (-b + math.sqrt(d))/2/a, (-b - math.sqrt(d))/2/a
    else:
        if d == 0:
            return -b/2/a, None
        else:
            return None, None

print(solve_quadratic_equation(5, 10, 0))