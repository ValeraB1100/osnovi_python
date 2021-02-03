from itertools import count, cycle


a = int(input("введите число с которого нужно начать вывод значений: "))
b = int(input("введите число которым закончится вывод значений: "))
for el in count(a):
    if el > b:
        break
    else:
        print(el)

c = input("введите что-нибудь для зацикливания: ")
d = int(input("введите количество повторов: "))
i = 0
for el in cycle(c):
    if i > d:
        break
    print(el)
    i += 1