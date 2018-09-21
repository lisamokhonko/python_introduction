#Task #32
#Написать функцию, которая выведет N самых часто встречающихся слов в файле.
# Для этого функция будет получать путь к файлу с текстом и кол-во самых часто встречающихся слов для печати.
#Поскольку в большинстве языков самыми часто используемыми словами являются союзы, предлоги, артикли и т.д.,
# то для литературных произведений данная функция вернет в top N слов именно их,
# что мало интересно с точки зрения анализа текста. Поэтому, кроме пути к файлу с текстом,
# необходимо в функцию передать путь к файлу с т.н. стоп-словами, которые необходимо исключить из подсчета.
# Пример файла с английским стоп-словами: https://github.com/dbradul/python_classes/blob/master/basics/stop2.txt
import pprint
import re
import operator

file_path_stop_words = r'C:\Users\lisam\Downloads\stop2.txt'
file_path_text = r'C:\Users\lisam\Downloads\galaxy.txt'
top_n = 20
def count_words(file_path_text, file_path_stop_words, top_n): # returns list of top_n most frequent words in file_path_text file, except words from file_path_stop_words file
    # words = {chr(code): 0 for code in range(ord("a"), ord("z") + 1)}
    # pprint.pprint(words)

    text = open(file_path_text).read()
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text_lst = text.split()
    text_to_analyze = list(text_lst)
    text_lst = list(set(text_lst))
    stop_words = open(file_path_stop_words).read()
    stop_words = stop_words.lower()
    stop_words = re.sub(r'[^\w\s]', '', stop_words)
    stop_words_lst = stop_words.split()
    stop_words_lst = list(set(stop_words_lst))
    words_dict = {word: 0 for word in text_lst if word not in stop_words_lst}
    #print(text_lst)
    #print(stop_words_lst)
    #words_dict = {word: 0 for word in text_lst}
    for word in text_to_analyze:
        if word in words_dict:
            words_dict[word] += 1
    #print(words_dict['galaxy'])
    #sorted_list = [{k, words_dict[k]} for k in sorted(words_dict, key=words_dict.get, reverse=True)]
    sorted_by_value = sorted(words_dict.items(), key=lambda kv: kv[1], reverse=True)
    # for key in sorted(words_dict.keys(), key=words_dict.get(key), reverse=True):
    #     print('%s -> %s' % (key, words_dict[key]))
    #pprint.pprint(sorted_by_value)
    result_list = []
    for i in range(top_n):
        result_list += sorted_by_value[i]
    print(result_list)
    return result_list
count_words(file_path_text, file_path_stop_words, top_n)