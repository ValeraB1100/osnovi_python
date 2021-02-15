class Cletka:
    def __init__(self, cletka1):
        self.cletka1 = cletka1

    def __add__(self, cletka2):
        return self.cletka1 + cletka2

    def __sub__(self, cletka2):
        if self.cletka1 - cletka2 > 0:
            return self.cletka1 - cletka2        #тут не понятно, если мешьше либо равно 0, то выдает сообщение
        else:                                             # и None, а так вроде нормально работает
            print("невозможно разъединить клетки")

    def __mul__(self, cletka2):
        return self.cletka1 * cletka2

    def __truediv__(self, cletka2):
        return self.cletka1 // cletka2

    def make_order(self, a):
        c = self.cletka1 // a            #количество рядов
        f = self.cletka1 % a             #количество ячеек в последнем ряду
        m = ("*" * a + "\\n") * c + "*" * f
        print(m)


d = Cletka(10)
print(d.__add__(10))
print(d.__sub__(10))
print(d.__mul__(10))
print(d.__truediv__(10))
d.make_order(5)
