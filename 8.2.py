class Retro(Exception):
    def __init__(self, number, number1):
        self.number= number
        self.number1 = number1
        # self.result = number /number1
    try:
        number, number1 = int
        number, number1 = int(number, number1)
        result = number / number1
        number = int and number1 > 0
        if number == 0:
            raise Exception("Это же ноль! делить на ноль нельзя")
    except Exception as rt:
        print("Это же ноль! делить на ноль нельзя")
    except ZeroDivisionError:
        print("Это же ноль! делить на ноль нельзя")
    except ValueError:
            print(" Вы ввели не число, нужно число")
    else:
        print(f'данные верны, резльтат {result}')
    finally: ("программа завершена")

a = Retro(10, 0)
