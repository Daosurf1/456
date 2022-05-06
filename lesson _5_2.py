# 2. Создать текстовый файл (не программно), сохранить в нём несколько
# строк, выполнить подсчёт строк и слов в каждой строке.

f = open("data_5_1.txt", 'r', encoding='utf-8')
cont = f.read().splitlines()
print('from file like this-',cont)
print('number of rows',len(cont))
z=0
for x in cont:
    len_of_each = len(x)
    z +=1
    print(f'len of row {z} =',len_of_each)
f.close()

