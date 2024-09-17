z = []
c: int | str
while z is not None:
    c = input('введите натуральное число, для окончания ввода введите enter :')
    if c== '':
        print('всего доброго :)')
        break
    else:
        c = int(c)
        z.append(c)
        z.sort()
        z.reverse()
        print(z)

