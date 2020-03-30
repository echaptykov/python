'''
    Урок 8 Задание 2
'''
class OwnError(Exception):
    def __init__(self,txt_error):
        self.txt_error = txt_error
try:
    int_a = int(input("Введите число А: "))
    int_b = int(input("Введите число Б: "))
    if int_b == 0:
        raise OwnError("Деление на 0!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат А / Б = {int_a / int_b}")