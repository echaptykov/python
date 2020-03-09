'''
Урок 2 Задание 2
'''
int_exit = 1
while int_exit != 0:
    li = 0
    user_list = []
    user_list = input("Введите элементы списка через пробел: ").split()
    user_list_len = len(user_list) // 2
    print("Список А: ",user_list)
    for i in range(user_list_len):
        user_list[li],user_list[li+1] = user_list[li+1],user_list[li]
        li += 2
    print("Список Б: ",user_list)
    str_user_data = input("Повторить? Enter-да. : ")
    if str_user_data != '':
        int_exit = 0
        print("Работа завершена.")