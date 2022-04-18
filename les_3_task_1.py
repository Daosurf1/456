def my_func1(x, y):
    res = 0
    try:
        res = x / y
    except ZeroDivisionError:
        print('второе число ноль')
    return res


a = int(input('делимое'))
s = int(input('введите делитель'))
print(my_func1(a, s))
