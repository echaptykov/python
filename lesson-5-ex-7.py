'''
    Урок 5 Задание 7
'''
import json
firm_dict = {}
profit_dict = {}
i_count = 0
i_sum = 0
average_profit = 0
try:
    with open("ex7.txt", 'r') as f_in:
        for line in f_in:
            firm_name,firm_f,firm_profit,firm_loss = line.split()
            firm_dict[firm_name] = int(firm_profit) - int(firm_loss)
            if firm_dict[firm_name] >= 0:
                i_sum = i_sum + firm_dict[firm_name]
                i_count += 1
    if i_count > 0:
        average_profit = i_sum / i_count
    profit_dict = {"average_profit" : average_profit}
    with open("ex7.json", "w") as write_f:
        json.dump([firm_dict, profit_dict], write_f)
    print("Работа завершена.")
except IOError:
    print("Ошибка ввода-вывода.")
except ValueError:
    print("Ошибка данных.")