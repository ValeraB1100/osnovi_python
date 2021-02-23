class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print("сложение")
        return f"c = {self.a + other.a} + {self.b + other.b}i"

    def __mul__(self, other):
        print("умножение")
        return f"c = {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}i"

    def __str__(self):
        return f"c = {self.a} + {self.b}i"


c_1 = Number(1, 2)
c_2 = Number(3, 4)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)