class Stationery:
    Title = "Title"

    def draw(self):
        return print("Старт отрисовки")

class Pen(Stationery):
    def draw(self):
        return print("Пишем ручкой!")


class Pencil(Stationery):
    def draw(self):
        return print("Рисуем карандашем!")


class Handle(Stationery):
    def draw(self):
        return print("Закрашиваем маркером!")


a = Stationery()
a.draw()

b = Pen()
b.draw()

c = Pencil()
c.draw()

d = Handle()
d.draw()