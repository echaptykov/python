'''
    Урок 4 Задание 5
'''

from functools import reduce
def my_func(arg_1, arg_2):
    return arg_1 * arg_2

my_list = [el for el in range(99, 1001) if el % 2 == 0]
print(f"{my_list}")
print(f"{reduce(my_func, my_list)}")
