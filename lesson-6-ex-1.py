'''
    Урок 6 Задание 1
'''
import time

class TrafficLight:
    __traffic_settings = {"Красный" : 7, "Жёлтый" : 2, "Зелёный" : 4}
    __traffic_mode = {"Красный" : "Жёлтый", "Жёлтый" : "Зелёный", "Зелёный" : "Красный"}
    __color = "Красный"

    def running(self,i_count):
        i = 0
        while i < i_count:
            print(self.__color)
            time.sleep(self.__traffic_settings.get(self.__color))
            self.__color = self.__traffic_mode.get(self.__color)
            i += 1
        print("Работа завершена")

traffic = TrafficLight()
traffic.running(6)