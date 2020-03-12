'''
    Урок 3 Задание 5
'''
int_sum = 0
def my_func(arg_1):
    global int_sum
    int_sum += sum([int(x) for x in arg_1.split()])
    return

int_exit = -1
try:
    while int_exit == -1:
        str_user_data = input("Введите строку чисел. Q - завершение работы. : ")
        int_exit = str_user_data.find('Q')
        if int_exit != -1:
            my_func(str_user_data[0:int_exit])
        else:
            my_func(str_user_data)
            print (f"Промежуточный итог: {int_sum}")
    print (f"Общий итог: {int_sum}")
except ValueError:
    print("Ошибка ввода данных.")


