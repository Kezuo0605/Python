# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def fun():
    num_1 = input("please enter first number")
    num_2 = int(input("please enter second number"))
    if num_1.isdigit() and num_1 >= "0":
        num_1 = round(int(num_1))
    else:
        print("please enter ONLY one uniqe number")
    if num_2 > 0:
        print("ok, lets start")
    else:
        try:
            num_2 = int(num_2)
            print(num_2)
        except ValueError:
            print("please enter ONLY one uniqe number")
        try:
            num_2 > 0
        except ZeroDivisionError:
            print("please Enter more than zero number")
        print("division by zero isnt correct, try again and be attention")
        num_2 = round(int(input("please, dear, enter only one round number above zero")))
    return num_1 / num_2


print(fun())


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def func(name, surname, yob, city, email, phone, ):
    dict1 = {"name": name, "surname": surname, "yearofbirth": yob, "city": city, "email": email, "phone": phone}
    for value in dict1:
        dict1[value] = input(f"enter {value}")
    return print(dict1)


func()


# 3. Реализовать функцию my_func(), которая принимает три
# позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    num = [num1, num2, num3]
    del num[min(num[:])]
    return print(sum(num))


my_func(9, 14, 2)


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def two(x, y):
    x = input(f" enter X number > 0")
    if x.isdigit() and x >= "0":
        x = round(int(x))
    else:
        try:
            x = int(x)
        except TypeError:
            print("please enter ONLY one uniqe number > 0")
    y = input(f" enter Y number < 0")
    if y.isdigit() and y < "0":
        y = round(int(y))
    else:
        try:
            y = int(y)
        except ValueError:
            print("please enter ONLY one uniqe number < 0")
    """Проверка на предмет корректности ввода"""
    y = y.__abs__()
    sub = (1 / x ** abs(y))
    return print(1 / x ** y)
"""Формула расчета"""

two(5, -5)

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
""" Программа не отлажена и не работает"""
def func():
    numbers = list(input("Enter numbers. Divide numbers by space. To finish program enter Q").split())
    n = numbers.count("Q")
    numbers = sum(numbers)

    while n == 0:
        numbers1 = list((input("Enter numbers. Divide numbers by space. To finish program enter Q").split()))
    numbers1 = sum(numbers1[:])
    numbers = [*numbers1, *numbers]
    numbers = sum(numbers[:])
    return print(numbers1, numbers)
func()
