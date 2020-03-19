'''
    Урок 5 Задание 1
'''
try:
    with open("out.txt", 'w') as f_out:
            str_out = input("Введите строку для записи в файл out.txt. Пустая строка - завершение : ")
            while str_out != '':
                f_out.write(str_out+'\n')
                str_out = input(": ")
except IOError:
    print("Ошибка ввода-вывода.")
