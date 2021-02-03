from math import factorial
#  этой библиотекой попробовал получить факториал просто ради интереса, не обращайте внимания


def fact(n):
    i = 1
    for b in range(1, n + 1):
        i *= b
        yield i


a = int(input("введите число для получения его факториала: "))
for el in fact(a):
    print(el)

print(factorial(a))
