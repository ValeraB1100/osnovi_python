def func(a, b):
    try:
        print(f"частное этих двух чисел равно: {a/b}")
    except ZeroDivisionError:
        print("на ноль делить нельзя")

a = int(input("введите первое число: "))
b = int(input("введите второе число: "))
func(a, b)