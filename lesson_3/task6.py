def int_func(lst):
    l = lst[0].upper()
    return l + lst[1:]
a = input("введите что-нибудь хорошее: ").split()
lst = []
for i in a:
    lst.append(int_func(i))
print(" ".join(lst))
