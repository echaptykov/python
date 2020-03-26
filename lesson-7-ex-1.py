'''
    Урок 7 Задание 1
'''
# поэлементное сложение двух списков
def list_sum(a,b):
    c=[]
    for x, y in zip(a,b):
        c += [ x + y ]
    if len(a) > len(b):
        c += a[len(a) - len(b) + 1:]
    elif len(a) < len(b):
        c += b[len(b) - len(a) + 1:]
    return c

class Matrix:

    def __init__(self, list_matrix):
        self.matrix = list_matrix

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in j]) for j in self.matrix])

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append(list_sum(self.matrix[i], other[i]))
        return Matrix(result)

matrix_1 = Matrix([[1,2,3],[4,5,6]])
matrix_2 = Matrix([[2,3,4],[5,6,7]])

print(f"Матрица 1 \n{matrix_1.__str__()}")
print(f"Матрица 2 \n{matrix_2.__str__()}")
print(f"Матрица 1 + Матрица 2 \n{matrix_1.__add__(matrix_2)}")



