def func(x, y):
    print(round(x**y, 2))
    i = -1
    b = x
    while i > y:
        x *= b
        i -= 1
    print(round(1/x, 2))
x = float(input("введите дейcтвительное положительное число: "))
y = int(input("введите целое отрицательное число: "))
func(x, y)