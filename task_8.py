#Task #8
#Дана строка с именем студента, в которой имя предшествует фамилии,
# например  ‘Mark Zuckerberg‘. Написать программу,
# которая преобразует эту строку, ставя фамилию на первое место,
# а имя на второе. Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.

name_to_split = 'Mark Zuckerberg'
first_name = name_to_split.split(' ')[0]
last_name = name_to_split.split(' ')[1]
print('Reverse name is',last_name, first_name)