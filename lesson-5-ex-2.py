'''
    Урок 5 Задание 2
'''

i_line_count = 0
i_word_count = 0
try:
    with open("out.txt", 'r') as f_in:
        for line in f_in:
            i_line_count += 1
            i_word_count = len(line.split())
            print(f"Строка {i_line_count} Cлов: {i_word_count}")
except IOError:
    print("Ошибка ввода-вывода.")
