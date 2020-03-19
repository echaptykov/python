'''
    Урок 5 Задание 3
'''
emp_wage = []
average_wage = 0
try:
    with open("staff.txt", 'r') as f_in:
        for line in f_in:
            emp_wage.append(line.split())
    for i in range(len(emp_wage)):
        emp_wage[i][1] = float(emp_wage[i][1])
        if emp_wage[i][1] < 20000 :
            print (emp_wage[i][0])
        average_wage += emp_wage[i][1]
    print (f"Средняя заработная плата: {average_wage / len(emp_wage):.2f}")
except IOError:
    print("Ошибка ввода-вывода.")
except ValueError:
    print("Ошибка в данных.")
except ZeroDivisionError:
    print("Ошибка в данных.")
