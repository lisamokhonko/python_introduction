#Task #33
#Определите сколько выжило пассажиров каждого пола и каждого класса кабины.
# Соотнесите это с общим числом пассажиров каждого пола и класса кабины.
# Таким образом, Вы определите как взаимосвязаны пол и класс кабины с выживаемостью.

import csv
import pandas as pd
import pprint as pp
from tabulate import tabulate

def get_data_from_csv(filename):

    f = open(filename, "r")
    list_dicts = [row for row in csv.DictReader(f, delimiter=',')]
    list_inner_dicts = [dict(row) for row in list_dicts]
    f.close()

    return list_inner_dicts


data_lst = get_data_from_csv(r'C:\Users\lisam\Downloads\titanic.csv')
dt = pd.DataFrame.from_dict(data_lst)
dt['Qty'] = 1

wanted_keys = ['Sex', 'Pclass', 'Survived', 'Qty']
dt_new = dt[wanted_keys]
wanted_keys[:] = ['Sex', 'Pclass', 'Survived']
#dt_new['Qty'] = 1
grouped = dt_new.groupby(wanted_keys).sum()
# print(grouped)
pp.pprint(grouped)
print(tabulate(grouped, headers='keys', tablefmt='psql'))