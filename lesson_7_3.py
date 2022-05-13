# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.


class Cell:
    def __init__(self, unit):
        self.unit = unit
        pass

    def make_order(self, line):
        str_cell = ['*' * line] * (self.unit // line)
        if self.unit % line:
            str_cell.append('*' * (self.unit % line))
        return '\n'.join(str_cell)

    def __str__(self):
        return f'{self.unit}'

    def __add__(self, other):
        print("Sum")
        return Cell(self.unit + other.unit)

    def __sub__(self, other):
        print(" subtraction")
        if self.unit < other.unit:
            raise ValueError('Units in first cell less then in second, subtraction is impossible ')
        return Cell(self.unit - other.unit)

    def __mul__(self, other):
        print("multiplication")
        return Cell(self.unit * other.unit)

    def __truediv__(self, other):
        print("division")
        return Cell(self.unit // other.unit)


w1 = Cell(7)
w2 = Cell(15)
w3 = Cell(4)
print(w1 + w2)
print(w2 - w1)
print(w1 * w2)
print(w1 / w2)
print(w1.make_order(3))