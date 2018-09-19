#Task #35
#Создать два класса: Окружность и Точка. Создать в классе окружности метод,
# который принимает в качестве параметра точку и проверяет находится ли данная точка внутри окружности.

import math
class Point:
    def __init__(self, x_point, y_point):
        self.x_point = x_point
        self.y_point = y_point

class Circle:
    def __init__(self, x_circle, y_circle, radius):
        self.x_circle = x_circle
        self.y_circle = y_circle
        self.radius = radius

    def is_point_in_circle(self, point):
        is_belong = True
        if math.sqrt(point.x_point - self.x_circle) + math.sqrt(point.y_point - self.y_circle) <= math.sqrt(self.radius):
            is_belong = True
        else:
            is_belong = False
        return is_belong

circle1 = Circle(0, 0, 5)
point1 = Point(10, 10)
print(circle1.is_point_in_circle(point1))