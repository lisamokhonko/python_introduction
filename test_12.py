#Test #12
#Для проверки остаточных знаний учеников после летних каникул,
# учитель младших классов решил начинать каждый урок с того,
# чтобы задавать каждому ученику пример из таблицы умножения,
# но в классе 15 человек, а примеры среди них не должны повторяться.
# В помощь учителю напишите программу, которая будет выводить на экран 15 случайных примеров из таблицы умножения
# (от 2*2 до 9*9, потому что задания по умножению на 1 и на 10 — слишком просты).
# При этом среди 15 примеров не должно быть повторяющихся (примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)

import random

def summer_test(): #-> list
	all_test_list = []
	unique_test_list = []
	duplicate_idx = []
	test_from = 2
	test_till = 9
	for i in range(test_from, test_till + 1):
		for j in range(test_from, test_till + 1):
			all_test_list.append([i, j, i*j])
	for i in range(len(all_test_list)):
		for j in range(len(all_test_list)):
			if (all_test_list[i][0] == all_test_list[j][1]) and (all_test_list[i][1] == all_test_list[j][0]):
				duplicate_idx.append(i)
				#print(all_test_list[i][0], all_test_list[j][1], ':', all_test_list[i][1], all_test_list[j][0])

	print(all_test_list)
	print(duplicate_idx)


summer_test()