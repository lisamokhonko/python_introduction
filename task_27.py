#Task #27

import re
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
    mixed_word = ''
    first_letter = ''
    last_letter = ''
    window_left = 1
    window_right = 0
    for elem in text_list:
        if len(elem) > 3:
            decoded_text = elem[0]
            last_letter = elem[-1]
            while window_right <= (len(elem) - 2):
                if window_left + 3 <= len(elem) - 2:
                    window_right = window_left + 3
                    mixed_word = list(elem)
                    mixed_word_part = mixed_word[window_left:window_right]
                    #print(mixed_word_part)
                    random.shuffle(mixed_word_part)
                    #print(mixed_word_part)
                    decoded_text += ''.join(mixed_word_part)
                    window_left = window_right
                    print(decoded_text)
                else:
                    pass
            #break
        else:
            decoded_text += elem + ' '
    print(decoded_text)

pemrtuate(text)