'''
    Урок 4 Задание 6 a)
'''
from sys import argv
from itertools import count
script_name, int_start = argv
print("Бесконечный итератор, генерирующий целые числа. Для следующего значение нажмите Еnter. Любой символ - выход")
try:
    for el in count(int(int_start)):
        print(f"{el}")
        if (input() != ''):
            break
except ValueError:
    print(f"Неверные параметры. lesson-4-ex-6a.py Стартовое_число.")