'''
    Урок 4 Задание 1
'''
from sys import argv
script_name, em_hours, em_rate, em_bonus = argv
try:
    print(f"Заработная плата = {int(em_hours) * float(em_rate) + float(em_bonus)}")
except ValueError:
    print(f"Неверные параметры. lesson-4-ex-1.py Количество_часов Почасовая_ставка Премия")