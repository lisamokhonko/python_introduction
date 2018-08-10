#Task #10
#Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'.
#В этой строке указаны имя писателя и через символ * даты рождения и смерти.
#Даты указаны в формате "YYYY-MM-DD". Требуется написать программу,
#которая по переданной строке определит возраст писателя
#и распечает его имя и возраст.
#Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна распечает:
#'Leo Tolstoy, 82'. Для строки 'Marcus Aurelius*121-04-26*180-03-17' - 'Marcus Aurelius, 59'.
#Примечание: Т.к. имена писателей могут быть разной длины,
#то индексы символов разделителей ('*', '-') будут разными!
#Месяцы и дни для определения возраста можно игнорировать.

string_to_split = 'Leo Tolstoy*1828-08-28*1910-11-20'
writer_name = string_to_split.split('*')[0]
writer_birth = string_to_split.split('*')[1]
writer_death = string_to_split.split('*')[2]
year_birth = int(writer_birth.split('-')[0])
year_death = int(writer_death.split('-')[0])
writer_age = year_death - year_birth
print('%s, %d' %(writer_name, writer_age))
