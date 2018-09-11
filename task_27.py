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
#text_list = text.split()
#print(text_list)

def pemrtuate(text): # returns permuted text
    text_list = text.split()
    decoded_text = ''
    mixed_word = ''
    for elem in text_list:
        if len(elem) > 3:
            #for i in range(len(elem)):
            mixed_word = list(elem)# + elem[-1])
            #print(mixed_word)
            mixed_word_part = mixed_word[1:-1]
            random.shuffle(mixed_word_part)
            #print(mixed_word_part)
            mixed_word = ''.join(mixed_word[0]) + ''.join(mixed_word_part) + ''.join(mixed_word[-1])
            #print(mixed_word)
            decoded_text += mixed_word + ' '
            continue
        else:
            decoded_text += elem + ' '
    print(decoded_text)

pemrtuate(text)