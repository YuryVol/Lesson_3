# 2.Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, lastname, year, city, email, phone):
    print(name, lastname, year, city, email, phone)

my_func(name= 'Yury', lastname='Vol', year='1981', city='Msc', email='email', phone='12345')