'''
    Урок 6 Задание 4
'''
class Car:
    def __init__(self,speed,color,name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"{self.name}: Скорость - {self.speed} км/ч")

    def go(self,speed):
        self.speed = speed

    def stop(self):
        self.speed = 0
        print(f"{self.name}: Остановка")

    def turn(self,direction):
        print(f"{self.name}: Поворот - {direction}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name}: Превышение допустимой скорости 60 км/ч")
        else:
            print(f"{self.name}: Скорость - {self.speed} км/ч")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name}: Превышение допустимой скорости 40 км/ч")
        else:
            print(f"{self.name}: Скорость - {self.speed} км/ч")

class SportCar(Car):
    def go(self):
        self.speed += 100

class PoliceCar(Car):
    def go(self, speed, lights_on = None):
        self.speed = speed
        if lights_on is not None:
            if lights_on:
                print(f"{self.name}: Мигалка включена. Ква-ква.")
            else:
                print(f"{self.name}: Мигалка выключена")

car_1 = TownCar(0,"Красный","Hyundai Solaris",False)
car_2 = WorkCar(0,"Синий","Газель",False)
car_3 = SportCar(0,"Чёрный","Ауди",False)
car_4 = PoliceCar(0,"Бело-синий", "Форд",True)

car_1.go(10)
car_2.go(10)
car_3.go()
car_4.go(20)
car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_4.show_speed()
car_1.go(50)
car_2.turn("Налево")
car_1.show_speed()
car_1.go(70)
car_1.show_speed()
car_4.go(70)
car_4.show_speed()
car_4.go(70,True)
car_1.stop()
car_4.stop()
