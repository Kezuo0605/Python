# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    name = "name"
    surname = "surname"
    position = "manager"
    wage1 = 15000
    bonus1 = 35000

    @staticmethod
    def inc (self):
        __income = {"wage": Worker.wage1, "bonus": Worker.bonus1}
        income1 = __income["wage"] + __income["bonus"]
        print(income1)

class Position (Worker):

    def get_full_name (self, name, surname):
        return print(f"Name - {name}, surname - {surname}")

    def get_total_income (self, wage, bonus):
        def inc(self):
            income1 = Worker.__income["wage"]+ Worker.income["bonus"]
            return print(income1)

a = Position()
a.get_full_name("Ivan", "Ivanov")

a.inc(1, 25000, 75000)


