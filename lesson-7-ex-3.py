'''
    Урок 7 Задание 3
'''
class Organic:
    def __init__(self,cells):
        self.cells = cells

    def __add__(self, other):
        return Organic(self.cells + other.cells)

    def __sub__(self, other):
        int_result = self.cells - other.cells
        if int_result <= 0:
            print("Операция Вычитание: Отрицательный результат")
        return Organic(int_result)

    def __mul__(self, other):
        return Organic(self.cells * other.cells)

    def __truediv__(self, other):
        return Organic(self.cells // other.cells)

    def make_order(self, row):
        str_result = ''
        return str_result.join("*" * row + "\n" for i in range(int(self.cells / row))) + "*" * (self.cells % row)

organic_1 = Organic(22)
organic_2 = Organic(5)
print(f"Клетка({organic_1.cells}) + Клетка({organic_2.cells}) = {(organic_1 + organic_2).cells}")
print(f"Клетка({organic_1.cells}) - Клетка({organic_2.cells}) = {(organic_1 - organic_2).cells}")
print(f"Клетка({organic_1.cells}) / Клетка({organic_2.cells}) = {(organic_1 / organic_2).cells}")

print(organic_1.make_order(5))