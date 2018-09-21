#Task #36
#Создать класс Транспортное средство и его потомков - классы Поезд и Самолет.
# В родительском классе должно быть определено минимум 1 конструктор, 3 атрибута и 1 метод.
# В классах-потомках должны быть добавлены минимум по 1 новому методу и по 1 новому атрибуту.
class Vehicle:
    def __init__(self, weight, max_capacity, max_speed):
        self.weight = weight
        self.max_capacity = max_capacity #Number of passangers that can get into Vehicle
        self.max_speed = max_speed
        self.current_capacity = 0

    def add_passanger(self, num_of_passanger):
        if (num_of_passanger + self.current_capacity) <= self.max_capacity:
            self.current_capacity += num_of_passanger
            print(num_of_passanger,'passangers were added')
        else:
            print('Not enough seats')


class Train(Vehicle):
    def __init__(self, weight, max_capacity, max_speed, num_vagons):
        super().__init__(weight, max_capacity, max_speed)
        self.num_vagons = num_vagons

    def add_vagon(self, vagon_to_add):
        self.num_vagons += vagon_to_add


class Aircraft(Vehicle):
    def __init__(self, weight, max_capacity, max_speed, max_distance):
        super().__init__(weight, max_capacity, max_speed)
        self.max_distance = max_distance

    def is_fly_distance(self, distance):
        can_fly = True
        if distance < self.max_distance:
            print('Aircraft can fly for such distance')
        else:
            print('Aircraft CAN NOT fly for such distance')
            can_fly = False
        return can_fly

vechicle1 = Vehicle(540000, 150, 300)
vechicle1.add_passanger(20)
vechicle1.add_passanger(30)
vechicle1.add_passanger(101)
print(vechicle1.current_capacity)

train1 = Train(100, 30, 70, 5)

plane1 = Aircraft(3000, 100, 150, 1500)
plane1.is_fly_distance(100)
train1.add_passanger(29)
train1.add_passanger(2)
train1.add_vagon(3)
print(train1.num_vagons)