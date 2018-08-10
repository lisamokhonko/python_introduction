#Task #9
#Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase.
# Для простоты считаем, что имя переменной всегда состоит из 3-х слов.
# Например: 'employee_first_name' -> 'EmployeeFirstName'

variable_snake = 'employee_first_name'
variable_list = variable_snake.split('_')
variable_camel = variable_list[0].title() + variable_list[1].title() + variable_list[2].title()
print('CamelCase for %s is %s' %(variable_snake, variable_camel))
