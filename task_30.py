#Task #30
#Написать функцию, возвращающую все простые числа от 1 до 100 в виде списка.
def gen_primes(): # returns list of ints
    lst = [2]
    #print(type(lst))
    for num in range(3, 101):
        prime = True
        for i in range(2, num):
            if (num%i == 0):
                prime = False
                break
        if prime:
           lst.append(num)
    return lst

print(gen_primes())