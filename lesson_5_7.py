# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


import json

with open('data 5_7.txt', 'r', encoding='utf') as f:
    z_profit = 0
    z_profit_id = 0
    z_loss = 0
    z_loss_id = 0
    profit = {}
    loss = {}
    for line in f:
        x = line.split(' ')
        z = int(x[2]) - int(x[3])

        if z > 0:
            z_profit += z
            z_profit_id += 1
            profit[x[0]] = z
        if z <= 0:
            z_loss += z
            z_loss_id += 1
            loss[x[0]] = z

        average_profit = {'average': z_profit / z_profit_id}
    fin = [loss, average_profit, profit]

    print(fin)
    js_average_profit = json.dumps(average_profit, ensure_ascii=False)
    js_profit = json.dumps(profit, ensure_ascii=False)
    js_loss = json.dumps(loss, ensure_ascii=False)
    with open('data 5_7_js.txt', 'w', encoding='utf') as f1:
        print(fin, file=f1)
