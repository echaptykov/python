'''
Урок 2 Задание 3
'''
int_exit = 1
month_dict = {1:"январь",2:"февраль",3:"март",4:"апрель",5:"май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
seasons_list = ["зима","весна","лето","осень"]
month_seasons_dict = {1:"зима",2:"зима",3:"весна",4:"весна",5:"весна",6:"лето",7:"лето",8:"лето",9:"осень",10:"осень",11:"осень",12:"зима"}
month_seasons_list = [0,0,1,1,1,2,2,2,3,3,3,0]
while int_exit != 0:
    user_month = int(input("Введите номер месяца: "))
    if user_month not in month_dict.keys():
        print("Вы ввели неверный номер месяца")
    else:
        print(f"LIST: Месяц {month_dict[user_month]}. Время года: {seasons_list[month_seasons_list[user_month-1]]}")
        print(f"DICT: Месяц {month_dict[user_month]}. Время года: {month_seasons_dict[user_month]}")
    str_user_data = input("Повторить? Enter-да. : ")
    if str_user_data != '':
        int_exit = 0
        print("Работа завершена.")