# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(x, y):
    z1 = x ** y
    r: int = 1
    z2: float = x
    y: float = abs(y)
    while r < abs(y):
        r += 1
        z2 = z2 * x
    z2 = 1 / (z2)
    return z1, z2


print(my_func(10, -3))
