# 5. Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from functools import reduce

with open('data 5_5.txt', 'w', encoding='utf')as f:
    print(5, 5, 5, 5, 1, 1, file=f)
with open('data 5_5.txt', 'r', encoding='utf')as f1:
    f1.seek(0)
    date = f1.read()

    print(reduce(lambda x, y: x + y, [int(i) for i in date.split(' ')]))
