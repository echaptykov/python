'''
    Урок 7 Задание 2
'''
from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    title = "Одежда"
    def __init__(self,param):
        self.param = param
    @abstractmethod
    def get_tissue_cons(self):
        pass

class Coat(AbstractClothes):
    title = "Пальто"
    def __init__(self,param):
        self.V = param
    @property
    def get_tissue_cons(self):
        return "Одежда-" + self.title + " " + str(self.V / 6.5 + 0.5)

class Costume(AbstractClothes):
    title = "Костюм"
    def __init__(self,param):
        self.H = param
    def get_tissue_cons(self):
        return super().title + "-" + self.title +" "+ str(2 * self.H + 0.3)

class Pants(AbstractClothes):
    title = "Штаны"

coat = Coat(52)
costume = Costume(1.8)

print(coat.get_tissue_cons)
print(costume.get_tissue_cons())

try:
    pants = Pants(0.9)
except TypeError:
    print("Класс Pants не имеет метода, определенного в родительском классе.")