# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().


def int_func(*args):
    print(args)
    d=[]
    for s in args:
        s = s.replace(s[0], s[0].upper(), 1)
        d.append(s)
    return d


c = input('введите слова с маленькой буквы через пробел:').split()
print(int_func(*c))
