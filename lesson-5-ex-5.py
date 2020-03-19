'''
    Урок 5 Задание 5
'''
from random import randint
i = 0
line = ''
try:
    with open("ex5.txt", 'w') as f_out:
        while i < 50:
            line += str(randint(0, 50))+' '
            i += 1
        f_out.write(line)
    print(f"Подготовлен файл с данными: {line}")
    with open("ex5.txt",'r') as f_in:
        f_data = f_in.read().split()
    print(f"Сумма чисел: {sum(map(int,f_data))}")
except IOError:
   print("Ошибка ввода-вывода.")
except ValueError:
   print("Ошибка данных.")
