# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов,
# передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import randint

class Car:
    speed = "speed"
    colour = "colour"
    name = "name"
    is_poice = True

    def go (self):
        print("машина поехала")
        go = (randint(1, 110))
        return print(f" Ехали {go} минут")

    def stop (self, speed):
        stop = (1 * self.speed * self.speed) / (254 / 0,7)
        return print(f" Тормозной путь {stop} метров(аs). При начальной скорости {self.speedspeed} км / ч")

    def show_speed(self):
        self.speed = randint (1,11) * 10
        return print(f'Скорость автомобиля сейчас {self.speed}')

    def turn(self):
        turn = randint (1, 11)
        if turn <= 5:
            print("Поворачиваем налево")
        else:
            print("Поворачиваем направо")


class TownCar(Car):
    def description(self):
        print("Машина для сельского жителя")

    def show_speed(self):
        self.speed = randint(1, 11) * 10
        if self.speed > 60:
            print("Превышение скорости")
        return print(f'Скорость автомобиля сейчас {self.speed}')

class WorkCar(Car):

    def description(self):
        print("городская машина для поездок на работу")

    def show_speed(self):
        self.speed = randint(1, 11) * 10
        if self.speed > 40:
            print("Превышение скорости")
        return print(f'Скорость автомобиля сейчас {self.speed}')

class SportCar(Car):
    def description(self):
        print("спортивная машина! Осторожнее на поворотах!")

class PoliceCar(Car):
    def description(self):
        print("Прижмитесь к обочине! положите руки на капот!")


a = TownCar()
a.show_speed()


b=SportCar()
b.show_speed()

c= WorkCar()
c.turn()

d = PoliceCar()
d.go()
d.show_speed()
d.description()

