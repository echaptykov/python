'''
    Урок 4 Задание 6 b)
'''
from sys import argv
from itertools import cycle
script_name = argv
print("Бесконечный итератор, повторяющий элементы списка. Для следующего значение нажмите Еnter. Любой символ - выход")
for el in cycle(['ABC',True,123]):
    print(f"{el}")
    if (input() != ''):
        break
