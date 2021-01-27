lst = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dct = {
    "зима": (12, 1, 2),
    "весна":(3, 4, 5,),
    "лето": (6, 7, 8),
    "осень":(9, 10, 11)
}
a = int(input("введите номер месяца: "))
if lst[0] == a or a <= lst[2]:
    print("сейчас зима")
if lst[3] <= a and a <= lst[5]:
    print("сейчас весна")
if lst[6] <= a and a <= lst[8]:
    print("сейчас лето")
if lst[9] <= a and a <= lst[11]:
    print("сейчас осень")

for i, j in dct.items():
    if a in j:
        print(i)