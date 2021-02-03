from random import randint


def generator(lst):
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            yield lst[i]


list0 = []
a = int(input("введите количество элементов в списке: "))
b = int(input("введите минимальный элемент списка: "))
c = int(input("введите максимальный элемент списка: "))
while len(list0) < a:
    list0.append(randint(b, c))
print(list0)
list1 = []
for el in generator(list0):
    list1.append(el)
print(list1)
