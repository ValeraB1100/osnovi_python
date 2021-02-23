class Exeption:
    def __init__(self, lst):
        self.lst = lst

    def func(self, a):
        while a != "stop":
            try:
                if type(int(a)) == int:
                    self.lst.append(int(a))
            except:
                print("введите число")
                
            a = input("")
        print(self.lst)

lst = []
ex = Exeption(lst)
a = input("")
ex.func(a)