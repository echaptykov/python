'''
Урок 2 Задание 5
'''
rate_list = [7,5,3,3,2]
int_exit = 1
print(f"Рейтинг: {rate_list}")
while int_exit != 0:
    int_user_rate = int(input("Введите новый элемент: "))
    rate_list.append(int_user_rate)
    rate_list.sort(reverse=True)
    print(f"Рейтинг: {rate_list}")
    str_user_data = input("Продолжить? Enter-да. : ")
    if str_user_data != '':
        int_exit = 0
        print("Работа завершена.")