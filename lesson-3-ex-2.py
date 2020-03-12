'''
    Урок 3 Задание 2
'''
def func_user_data (name, surname, birth_year, city, e_mail, phone):
    return " ".join([name, surname, str(birth_year), city, e_mail, phone])

print(f'Пользователь: {func_user_data("Владимир","Петров",1998,"Санкт-Петербург","vpetrov@mail.ru","+79125111222")}')