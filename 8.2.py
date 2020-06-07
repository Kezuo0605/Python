
class retro (Exception):
    def __init__(self, number, number1):
        self.number= number
        self.number1 = number1
        self.result = number /number1


        try:
            number, number1= int(number, number1)
            result = number / number1
            number = int and number1 > 0
            if number1 or number < 0:
                raise retro ("Ввели число меньше ноля")
        except ZeroDivisionError:
            print("Это же ноль! делить на ноль нельзя")
        except ValueError:
            print (" Вы ввели не число, нужно число")
        except retro as rt:
            print(rt)
        else:
            print(f'данные верны, резльтат {result}')
        finally: ("программа завершена")


a = retro (12, 6)