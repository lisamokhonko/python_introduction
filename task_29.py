#Task #29
#Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
#Пароль состоит из 8 символов
#В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
#Пароль обязательно должен содержать Большие и маленькие буквы и цифры

import random

def gen_password(): # returns string
    psw = ''
    # предварительно создаем переменную
    for _ in range(8):
        psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_'))
    return psw

print(gen_password())