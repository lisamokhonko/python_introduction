#Task #16
#Два поезда движутся на скорости V1 и V2 навстречу друг другу.
#Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
#При заданных скоростях узнать столкнутся ли поезда.

#Предположим, что скорость поездов измеряется в км/час
def have_trains_crashed(v1, v2): # returns boolean value
    full_path = 10
    s1 = 4
    t1 = s1/v1
    s2 = v2*t1
    if s2 < (full_path - s1):
        return False
    else:
        return True

print(have_trains_crashed(5, 5))