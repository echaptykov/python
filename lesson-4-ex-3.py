'''
    Урок 4 Задание 3
'''
print(f"Числа в пределах от 20 до 240, кратные 20 или 21 : {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}")