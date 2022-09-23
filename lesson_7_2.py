# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    total_its = 0
    total_exp = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Clothes.total_its += 1
        Clothes.total_exp += self.expense

    def __str__(self):
        return f'Пальто, размер {self.size}, израсходовано {self.expense}, всего вещей {Clothes.total_its} , всего ' \
               f'израсходованно {Clothes.total_exp} '


    @property
    def expense(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Clothes.total_its += 1
        Clothes.total_exp += self.expense

    def __str__(self):
        return f'Костюм, рост  {self.height}, израсходовано  {self.expense}, всего шт {Clothes.total_its} , всего ' \
               f'израсходованно {Clothes.total_exp} '

    @property
    def expense(self):
        return round(self.height * 2 + 0.3, 2)


c1 = Coat(26)
c2 = Coat(31)
c3 = Suit(1.63)
c4 = Suit(1.79)

print(c1)
print(c2)
print(c3)
print(c4)


