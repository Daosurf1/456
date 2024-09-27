# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.
def my_func(x, c, v, ):
    list2max = [x, c, v]
    list2max = sum(list2max) - min(list2max)
    return list2max


print(my_func(6, 2, 1))
