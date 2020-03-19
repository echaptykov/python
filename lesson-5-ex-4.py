'''
    Урок 5 Задание 4
'''
en_rus_dict = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}
try:
    with open("ex4_in.txt", 'r') as f_in:
        with open("ex4_out.txt",'w') as f_out:
            for line in f_in:
                if line != '\n':
                    en_key = line.split(' - ')
                    f_out.write(en_rus_dict[en_key[0]] + " - "+ en_key[1])
                else:
                    f_out.write(line)
except IOError:
    print("Ошибка ввода-вывода.")
except ValueError:
    print("Ошибка данных.")
