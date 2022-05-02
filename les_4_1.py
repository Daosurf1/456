from sys import argv

print(argv[1:])
print('сумма',sum([int(el) for el in argv[1:]]))


