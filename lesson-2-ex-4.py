'''
Урок 2 Задание 4
'''
int_exit = 1
while int_exit != 0:
    user_list = []
    user_list = input("Введите строку: ").split()
    user_list_len = len(user_list)
    for i in range(user_list_len):
        print(f"{i+1} {user_list[i] [0:10]}")
    str_user_data = input("Повторить? Enter-да. : ")
    if str_user_data != '':
        int_exit = 0
        print("Работа завершена.")