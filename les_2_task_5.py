# задание 5
# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
c = int(input('Введите натуральное число'))
my_list.append(c)
my_list.sort()
my_list.reverse()
print(my_list)