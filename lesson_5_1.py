

print('введите значения для записи в файл, пустой ввод завершит операцию')

date_in = str
f = open("data_5_1.txt", 'w', encoding='utf-8')
while date_in != '':
    date_in = input()
    print(date_in, file=f)
f.close()
