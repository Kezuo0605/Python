from abc import  ABC

class Warehouse(ABC):
    def __init__(self, quantity, cost,  price, name, marge, type):
        self.quantity = quantity
        self.cost = cost
        self.price = price
        self.name = name
        self.type = type
        self.fullSku = {name: self.name, type:self.type, price:self.price, quantity:self.quantity},

    def __str__(self):
        return f' прайс-лист магазина магазина: наименование товара {self.name}, стоимость {self.price}, доступное к заказу количество на складе {self.weight}'

    #@abstractmethod
    def __price__(self,cost, marge):
        price = self.cost * self.marge
        return print(price)

    def Wh (self):
        try:
            type = input(f'Enter type of eqipment (printer, scaner, kopier). to exit enter q')
            while type != 'q':
                cost = int(input(f'Enter cost '))
                quantity = int(input(f'enter quantity '))
                fullSku = {'Type': type, 'cost': cost, 'quantity': quantity}
                sku = []
                sku = sku.append(fullSku).split()
                return print(f'Текущий список -\n {self.sku}')
        except:
            return f'error of data'
        finally:
            return print("the end")

    def __str__(self):
        return f' Перечень оборудования {self.name}, стоимость {self.price}, доступное к заказу количество на складе {self.weight}'

class Eq(Warehouse):

    @property
    def price (self):
        return self.__price

    @price.setter
    def price (self, cost):
        if cost <= 1900:
            self.__price = cost * 2
        elif cost > 1900 and self.cost <= 2300 :
            self.__price = self.cost *1,6
        else:
            self.__price = self.cost * 1,2

class Printer (Eq):

    def price (self,cost):
        price = int(self.cost * 1,3)
        return print (price)
    pass

class Scanner (Eq):

    def __str__(self):
        return f' прайс-лист магазина магазина: наименование товара {self.name}, стоимость {self.price}, доступное к заказу количество на складе {self.weight}'


class Kopier (Eq):
    pass




