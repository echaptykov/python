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
        yield factorial(i)

fibo_gen = generator_range()
for el in fibo_gen:
    print(el)

fibo_gen = generator_count()
i = 1
for el in fibo_gen:
    if i > 15:
        print("Работа завершена")
        break
    i += 1
    print(el)
