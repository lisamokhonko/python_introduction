#Task #15
#Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
#Каждая окружность задается координатами центра и радиусом.

import math

def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
    d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    #No Intersection
    if d > abs(r1 + r2) or d < abs(r1 - r2):
        return False
    else:
        return True
    # 1 point
    #d == abs(r1 + r2) or d == abs(r1 - r2)
    #2 points
    #d < abs(r1 + r2) or d > abs(r1 - r2)

print(circles_intersect(2,2,5,2,2,2))