#Task #24
#Для удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы
#в зависимости от первых букв их фамилии. Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’.
#Название группы определяет в какую группу попадает абитуриент, в зависимости от первой
#буквы его/ее фамилии. Например, Will Smith попадает в группу ‘Q-T’, т.к. первая буква его
#фамилии попадает в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).
#Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д. Написать функцию,
#которая получает список имен студентов вида ['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...]
#и возвращает количество абитуриентов в группах, сформированных по их фамилиям, описанным выше образом.

list_of_enrollees = ['Jeff Bezos', 'Will Smith', 'Gavin Belson', 'Leonard Hofsteder', 'Buzz Aldrin']

def group_by_surname(list_of_enrollees): # returns 4 ints
    a_i = 0
    j_p = 0
    q_t = 0
    u_z = 0
    for elem in list_of_enrollees:
        last = elem.split()[1]
        last_initial = last[0]
        if last_initial >= 'A' and last_initial <= 'I':
            a_i += 1
        elif last_initial >= 'J' and last_initial <= 'P':
            j_p += 1
        elif last_initial >= 'Q' and last_initial <= 'T':
            q_t += 1
        elif last_initial >= 'U' and last_initial <= 'Z':
            u_z += 1
    return a_i, j_p, q_t, u_z


print('A-I: %d, J-P: %d, Q-T: %d, U-Z: %d' % group_by_surname(list_of_enrollees))