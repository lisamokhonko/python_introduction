#Task #29
#Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
#Пароль состоит из 8 символов
#В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
#Пароль обязательно должен содержать Большие и маленькие буквы и цифры

import random

def gen_password(): # returns string
    symbols_letters_upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    symbols_letters_lower = 'qwertyuiopasdfghjklzxcvbnm'
    symbols_digits = '0123456789'
    passkey = ''
    passkey += passkey.join(random.choice(symbols_letters_upper))
    passkey += passkey.join(random.choice(symbols_letters_lower))
    passkey += passkey.join(random.choice(symbols_digits))
    symbols_letters_upper = symbols_letters_upper.join('_')
    #print(passkey)
    for i in range(5):
        if random.choice([1, 2, 3]) == 1:
            passkey += passkey.join(random.choice(symbols_letters_upper))
        elif random.choice([1, 2, 3]) == 2:
            passkey += passkey.join(random.choice(symbols_letters_lower))
        else:
            passkey += passkey.join(random.choice(symbols_digits))
    return ''.join(random.sample(passkey, len(passkey)))

print(gen_password())
