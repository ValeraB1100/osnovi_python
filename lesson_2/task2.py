lst = []
while True:
    a = input("введите число или exit для прекращения ввода: ")
    if a == "exit":
        break
    lst.append(a)
print(lst)
for i in range(1, len(lst), 2):
    lst[i], lst[i-1] = lst[i-1], lst[i]
print(lst)