# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Осуществить вывод данных о пользователе одной строкой.


def human(city_living4, name1, year_birth3, email5, surname2, telefon6, x=None):
    if x is None:
        list_of_man = [name1, surname2, year_birth3, city_living4, email5, telefon6]
    return list_of_man


name = input('введите имя ')
surname = input("введите фамилию ")
year_birth = input("введите год рождения ")
city_living = input("введите город проживания ")
email = input("введите email ")
telefon = input("введите телефон ")

print(human(name1=name, surname2=surname, year_birth3=year_birth, email5=email, city_living4=city_living, telefon6=telefon))
