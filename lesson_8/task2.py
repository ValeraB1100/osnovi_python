class Exeption:
    @staticmethod
    def func(a, b):
        try:
            print(a//b, a%b, a/b)
        except ZeroDivisionError:
            print("на ноль делить нельзя")

Exeption.func(12, 1)