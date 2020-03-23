'''
    Урок 6 Задание 5
'''
class Stationery:
    def __init__(self,title):
        self.title = title
    def draw(self):
        print("Draw базового класса")

class Pen(Stationery):
    def draw(self):
        print(f"{self.title} - метод класса Pen")

class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} - метод класса Pencil")

class Handle(Stationery):
    def draw(self):
        print(f"{self.title} - метод класса Handle")

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()