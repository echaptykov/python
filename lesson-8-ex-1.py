'''
    Урок 8 Задание 1
'''
class MyData:
    str_data =''
    def __init__(self,str_data):
        self.str_data = str_data
    @classmethod
    def extract_num(cls,str_data):
        return list(map(int,(str_data.split("-"))))
    @staticmethod
    def valid_data(str_data):
        num_data = MyData.extract_num(str_data)
        if num_data[0] / 31 > 1:
            print ("Ошибка! День.")
        if num_data[1] / 12 > 1:
            print ("Ошибка! Месяц.")
        return num_data

print(MyData.extract_num("10-04-1980"))
data_1 = MyData("05-11-2019")
print(data_1.valid_data("01-14-1970"))
