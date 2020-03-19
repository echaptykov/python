'''
    Урок 5 Задание 6
'''
les_dict = {}
def get_hours(str_data):
    if str_data == '—':
        return 0
    else:
        return int(str_data[0:str_data.find("(")])
try:
    with open("ex6.txt", 'r') as f_in:
        for line in f_in:
            int_hours = 0
            les_name,les_l,les_p,les_t = line.split()
            int_hours += get_hours(les_l)+get_hours(les_p)+get_hours(les_t)
            les_dict[les_name]= int_hours
    print(f"{les_dict}")
except IOError:
    print("Ошибка ввода-вывода.")
except ValueError:
    print("Ошибка данных.")