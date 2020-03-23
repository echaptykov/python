'''
    Урок 6 Задание 2
'''
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self,mass_per_sm, thickness):
        return self._length * self._width * mass_per_sm * thickness

r = Road(20,5000)

print(f"{r.mass(25,5) / 1000}т.")
print(f"{r.mass(10,2) / 1000}т.")