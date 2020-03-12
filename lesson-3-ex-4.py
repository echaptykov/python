'''
    Урок 3 Задание 4
'''
def my_func(x,y):
    return x ** y

def my_func_1(x,y):
    my_pow = 1
    for i in range(abs(y)):
        my_pow = my_pow / x
    return my_pow

print(pow(6,-2))
print(my_func(6,-2))
print(my_func_1(6,-2))