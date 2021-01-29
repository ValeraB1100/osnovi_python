def my_func(a,b,c):
    lst = [a,b,c]
    lst.pop(lst.index(min(lst)))
    print(f"сумма наибольших двух чисел равна: {sum(lst)}")
a = int(input("введите число: "))
b = int(input("введите число: "))
c = int(input("введите число: "))
my_func(a,b,c)