'''
    Урок 4 Задание 7
'''
from math import factorial
from itertools import count

def generator_range():
    for i in (range(1,16,1)):
        yield factorial(i)

def generator_count():
    for i in count(1):
        if i < 16:
            yield factorial(i)
        else:
            print('Работа завершена')
            return

fibo_gen = generator_range()
for el in fibo_gen:
    print(el)

fibo_gen = generator_count()
for el in fibo_gen:
    print(el)