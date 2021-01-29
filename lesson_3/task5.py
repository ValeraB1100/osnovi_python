def func(sum, lst):
    for i in range(len(lst)):
        sum += int(lst[i])
    return sum
sm = 0
a = input("введите числа через пробел: ").split()
while a != "q":
    sm = func(sm, a)
    print(sm)
    a = input("введите числа через пробел или q для выхода: ").split()
    if "q" in a:
        a.remove("q")
        sm = func(sm, a)
        print(sm)
        break
