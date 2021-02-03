from random import randint

# почему в этот генератор выдает значения по возрастанию?
# def generator(lst):
#     for i in range(len(lst)):
#         if lst.count(i) == 1:
#             yield i


list0 = []
a = int(input("введите количество элементов в списке: "))
b = int(input("введите минимальный элемент списка: "))
c = int(input("введите максимальный элемент списка: "))
while len(list0) < a:
    list0.append(randint(b, c))
print(list0)


# а почему этот генератор выдает значения в том порядке, в котором они были в исходном списке?
list1 = [el for el in list0 if list0.count(el) == 1]
# for el in generator(list0):
#     list1.append(el)
print(list1)
