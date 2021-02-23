class Sclad:
    def __init__(self, name, cena, col, lst):
        self.name = name
        self.cena = cena
        self.col = col
        self.lst = []
        self.full_lst = lst

    def __str__(self):
        return f"{self.name} цена {self.cena} количество {self.col}"

    def func(self):
        try:
            a = {"Модель устройства": input(f"Введите наименование "),
                      "Цена за ед": int(input(f"Введите цену за ед ")),
                      "Количество": int(input(f"Введите количество "))}
            self.lst.append(a)
            print(f"текущий список \n {self.lst}")
        except:
            return f"ошибка при вводе"

        print("Для выхода введите -1")
        q = input("")
        if q == "-1":
            self.full_lst.append(self.lst)
            print(f"на складе\n {self.full_lst}")
        else:
            return Sclad.func(self)

class Printer(Sclad):
    def __str__(self):
        return  f"на складе принтеров {lst[0]}"
class Scaner(Sclad):
    def __str__(self):
        return f"на складе сканеров {lst[1]}"
class Xerox(Sclad):
    def __str__(self):
        return f"на складе ксероксов {lst[2]}"

lst = []
a = Printer("принтер", 300, 1, lst)
b = Scaner("сканер", 470, 2, lst)
c = Xerox("ксерокс", 1000, 3, lst)
print(a.func())
print(b.func())
print(c.func())
print(a)
print(b)
print(c)