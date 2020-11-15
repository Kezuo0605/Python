"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

import collections
import timeit

list_with_range = [el for el in range(1000)]
deque_with_range = deque()
deque_with_range.extend(list_with_range)

def list_append(num):
    my_list = []
    for i in range(num):
        my_list.append(i)

def deque_append(num):
    my_list = deque()
    for i in range(num):
        my_list.append(i)

def list_appendleft(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)

def deque_appendleft(num):
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)

def list_extend(lst_range):
    my_list = []
    my_list.extend(lst_range)

def deque_extend(lst_range):
    my_list = deque()
    my_list.extend(lst_range)

def list_extendleft(lst_range):
    my_list = []
    for el in lst_range:
        my_list.insert(0, el)

def deque_extendleft(lst_range):
    my_list = deque()
    my_list.extendleft(lst_range)

def list_reverse(lst_range):
    a = lst_range.reverse()

def deque_reverse(lst_range):
    a = lst_range.reverse()
