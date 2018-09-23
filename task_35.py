#Task #35
#Создать два класса: Окружность и Точка. Создать в классе окружности метод,
# который принимает в качестве параметра точку и проверяет находится ли данная точка внутри окружности.

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def is_point_in_circle(self, point):
        is_belong = True
        if math.sqrt(pow((point.x - self.x), 2)) + math.sqrt(pow((point.y - self.y), 2)) <= math.sqrt(pow(self.radius, 2)):
            is_belong = True
        else:
            is_belong = False
        return is_belong

circle1 = Circle(0, 0, 5)
point1 = Point(1, 1)
p = Point(0, 0)
c = Circle(1, 1, 1)
print(circle1.is_point_in_circle(point1))
print(c.is_point_in_circle(p))