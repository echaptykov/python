'''
 Урок 3 Задание 1
'''
def func_div (var_1,var_2):
    try:
        return float(var_1) / float(var_2)
    except ZeroDivisionError:
        return "Деление на 0"
    except ValueError:
        return "Аргументами функции должны быть числа"
int_exit = 1
while int_exit != 0:
    fl_rez = func_div(input("Введите число X:"), input("Введите число Y: "))
    print(f"X / Y = {fl_rez}")
    str_user_data = input("Продолжить? Enter-да. : ")
    if str_user_data != '':
        int_exit = 0
        print("Работа завершена.")


