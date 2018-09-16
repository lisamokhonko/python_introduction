#Test #6
#Определить является ли строка изограммой (https://en.wikipedia.org/wiki/Isogram ), т.е. что все буквы в ней
# за исключением пробелов встречаются только один раз. Например, строки 'Питон', 'downstream', 'книга без слов'
# являются изограммами, а само слово 'изограмма' - нет.

import re

str_to_check = 'книга без слов0'

def is_isogram(str_to_check): #-> bool
    list_checked = []
    str_to_check = ''.join(str_to_check.split())
    for char in str_to_check:
        if char not in list_checked:
            list_checked.append(char)
        else:
            return False
    return True

print(is_isogram(str_to_check))