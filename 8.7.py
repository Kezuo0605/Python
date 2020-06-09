"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата."""

class Complexnumbers():
    def __init__ (self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        complex = real + (i * imaginary)
        i = 'i'
        # self.real2 = -10
        # self.imaginary2 = -6

    def __add__ (self, other):
        return print(((self.real + other.real), (self.imaginary + other.imaginary) ))

    def __mul__(self,other):
        return print (self.real * other.real)+(self.imaginary*other.imaginary)+(self.imaginary * other.imaginary)

z = Complexnumbers(12, 345)
z2 = Complexnumbers(234, -9856)

print(z + z2)
print(z * z2)


