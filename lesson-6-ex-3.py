'''
    Урок 6 Задание 3
'''
class Worker:
    def __init__(self):
        self.name = "Исаев"
        self.surname = "Максим"
        self._position = "Штандартенфюрер"
        self._income = {"wage" : 1000, "bonus" : 500}

class Position(Worker):
    def get_full_name(self):
        print(self._position + " " + self.name + " " + self.surname)
    def get_total_income(self):
        print(f"Доход: {self._income.get('wage') + self._income.get('bonus')}")

w1 = Position()
w2 = Position()

w2.name = "Борман"
w2.surname = "Мартин"
w2._position = "Партайгеноссе"
w2._income.update({"wage" : 1500})

w1.get_full_name()
w1.get_total_income()

w2.get_full_name()
w2.get_total_income()
