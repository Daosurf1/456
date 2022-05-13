# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# ко яФЯЯЧЯ1Й2Йторый должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8


class Matrix:

    def __init__(self, data):
        self.data = data
        for line in self.data[:-1]:
            if not len(line) == len(self.data[self.data.index(line) + 1]):
                raise ValueError('Количество элементов в строках не совпадает ')

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.data)

    def __add__(self, other):
        if not len(self.data) == len(other.data):
            raise ValueError('размерности матриц не совпадают ')
        else:
            for i in range(len(self.data)):
                item = [[int(self.data[line][num]) + int(other.data[line][num])
                         for num in range(len(self.data[line]))]
                        for line in range(len(self.data))]
                return Matrix(item)


m1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
m2 = [[4, 4, 4], [5, 5, 5], [6, 6, 6]]

mt1 = Matrix(m1)
mt2 = Matrix(m2)
print(mt1)
print('-' * 35)
print(mt2)
print('-' * 35)

print(mt1 + mt2)
