# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from functools import reduce

with open("data_5_4.txt", 'r', encoding='utf-8') as f:
    with open("data_5_4_1.txt", 'w', encoding='utf-8') as z:
        res_dict = dict((a.strip(), int(b.strip()))
                        for a, b in (line.split('—')
                                     for line in f))

        res_dict['Один'] = res_dict.pop('One')
        res_dict['Два'] = res_dict.pop('Two')
        res_dict['Три'] = res_dict.pop('Three')
        res_dict['Четыре'] = res_dict.pop('Four')
        for i, k in res_dict.items():
            print(i, '-', k, file=z)

