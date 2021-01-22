#для проверки задач раскомментируйте нужную задачу

#task 1

#i = 1
#y = 3
#r = int(input("введите число: "))
#d = input("введите что-нибудь: ")
#print(i, y, r, d)

#task 2

# time = int(input("введите время в секундах: "))
# h = time // 3600
# m = time % 3600 // 60
# s = time % 3600 % 60
# print("ваше время: {}:{}:{}".format(h, m, s))

#task 3

# n = input("введите число: ")
# print("сумма n+nn+nnn равна: " + str(int(n) + int(n*2) + int(n*3)))

#task 4

# c = input("введите число: ")
# q = len(c)
# w = 0
# b = 0
# while w < q:
#     if int(c[w]) > b:
#         b = int(c[w])
#     w += 1
# print(b)

#task 5
#
# doh = int(input("введите выручку фирмы: "))
# ras = int(input("введите издержки фирмы: "))
# res = doh - ras
# if res > 0:
#     print("ваши доходы составили: " + str(res) + " руб.")
#     rent = res / doh
#     print("рентабильность: " + str(rent))
#     kol = int(input("введите количество сотрудников: "))
#     print("прибыль фирмы в расчете на одного сотрудника составила: " + str(res / kol) + " руб.")
# else:
#     print("вы ушли в минус на: " + str(res) + " руб.")

#task 6

# a = int(input("введите результат первого дня: "))
# b = int(input("введите результат, день которого вы хотите узнать: "))
# l = 1
# while a < b:
#     print(str(l) + "-й день: " + str(a))
#     a = a * 1.1
#     l += 1
# print(a)