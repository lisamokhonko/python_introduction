#Test
#Task 1

def task_1(a, b, c):
    return (a + b*c)**2

print(task_1(2, 3, 3))

def task_2(a, b, c):
    if c == 0:
        return 'Error: division by zero'
    else:
        return a - 4*b/c

print(task_2(2, 3, 0))

def task_3(a, b, c):
    if c == 1:
        return 'Error: division by zero'
    else:
        return (a*b + 4)/(c - 1)

print(task_3(2, 3, 1))
