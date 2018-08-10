#Task #7
#Преобразовать строку с американским форматом даты в европейский.
# Например, '05.17.2016' преобразуется в '17.05.2016'
import datetime

#Option 1. Work with String
date_for_split = '05.17.2016'
date_for_split_lst = date_for_split.split('.')
date_eu = date_for_split_lst[1] + '.' + date_for_split_lst[0] + '.' + date_for_split_lst[2]
print('European format for %s is %s' %(date_for_split, date_eu))

#Option 2. Work with Date
format_str = '%m.%d.%Y'
datetime_obj = datetime.datetime.strptime(date_for_split, format_str)
date_date_eu = datetime.datetime.strftime(datetime_obj,'%d.%m.%Y')
print('European format for %s is %s' %(date_for_split, date_date_eu))
