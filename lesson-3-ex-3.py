'''
    Урок 3 Задание 3
'''
def my_func(arg_1, arg_2, arg_3):
    return sum([arg_1,arg_2,arg_3]) - min([arg_1,arg_2,arg_3])

print(f"1 -4 5 : {my_func(1, -4, 5)}")
print(f"10 7 4 : {my_func(10, 7, 4)}")