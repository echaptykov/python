'''
Урок 2 Задание 6
К сожалению, из текста задания не совсем понятно, обрабатываем уже готовую структуру или можно
формировать словарь аналитики при вводе структуры. Решил обрабатывать готовую структуру.
'''
goods_str = []
int_exit = 1
goods_num = 0
while int_exit != 0:
    goods_num += 1
    goods_dict = {'название': '', 'цена': 1,'количество': 1, 'ед': ''}
    for dict_key in goods_dict.keys():
        while True:
            try:
                str_user_data  = input(f"Введите значение {dict_key}: ")
                if dict_key == "количество":
                    goods_dict[dict_key] = int(str_user_data)
                elif dict_key == "цена":
                    goods_dict[dict_key] = float(str_user_data)
                else:
                    goods_dict[dict_key] = str_user_data
                break
            except ValueError:
                print('Введите, пожалуйста, число')
    goods_str.append((goods_num, goods_dict))
    str_user_data = input("Добавить ещё товар? Enter-да. : ")
    if str_user_data != '':
        int_exit = 0
print("Структура товаров:")
for good in goods_str:
    print(good)
'''
Обрабатываем готовую структуру
Этот кусочек подсмотрел у кого-то из студентов. В первом варианте у меня было 4 списка, а потом из них я делал
словарь.
'''
analytics_dict={}
for good in goods_str:
    for an_key,an_value in good[1].items():
        if an_key in analytics_dict:
            analytics_dict[an_key].append(an_value)
        else:
            analytics_dict[an_key]=[an_value]
'''
Оставляем в словаре только уникальные значения характеристик и выводим на экран. Можно было делать это и в предыдущем цикле, через проверку in.
'''
print("Аналитика:")
for dict_key in analytics_dict.keys():
    analytics_dict[dict_key]=list(set(analytics_dict[dict_key]))
    print(f"{dict_key}: {analytics_dict[dict_key]}")
