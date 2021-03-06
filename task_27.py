#Task #27

import re
import math
import random

text = '''
Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную, 
на первый взгляд, награду: столько пшеничных зёрен, сколько окажется на шахматной доске, 
если на первую клетку положить одно зерно, на вторую — два зерна, 
на третью — четыре зерна и т. д. Оказалось, что такого количества зерна нет на всей планете
'''
text = re.sub(r'[^\w\s]','',text)
#text = 'Согласно'
#text_list = text.split()
#print(text_list)


def pemrtuate(text): # returns permuted text
    text_list = text.split()
    decoded_text = ''
    window = 3

    def permtuate_word(word):
        first, last = word[0], word[-1]
        decoded_word = ''
        middle = word[1:-1]
        old_i = 0
        sub_middle_sh = ''

        for i in range(math.ceil(len(middle) / window)):
            sub_middle = list(middle[old_i:old_i + window])
            random.shuffle(sub_middle)
            sub_middle_sh = ''.join(sub_middle)
            old_i += window
            decoded_word += sub_middle_sh
        decoded_word = first + decoded_word + last
        return decoded_word

    for elem in text_list:
        if len(elem) > window:
            decoded_text += permtuate_word(elem) + ' '

        else:
            decoded_text += elem + ' '
    return decoded_text

print(pemrtuate(text))