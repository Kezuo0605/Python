"""1. Создать класс TrafficLight (светофор) и определить у него один
атрибут color (цвет) и метод running (запуск). Атрибут реализовать
как приватный. +
В рамках метода реализовать переключение светофора
в режимы: красный, желтый, зеленый.
Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав
экземпляр и вызвав описанный метод.
"""
import time
from itertools import cycle


class TrafficLight:
    _TrafficLight_colour = "цвет"

    # VAr2
    # @staticmethod
    def running(self):
        _cred = "красный"
        _corange = "оранжевый"
        _cgreen = "зеленый"
        _fub = [_cred, _corange, _cgreen, _corange]
        for i in cycle(_fub):
            print(i)
            time.sleep(2) if i == "оранжевый" else time.sleep(7)
Var1 = TrafficLight()
print(Var1)
Var1.running()

# VAR2:
# TrafficLight.running(1)
