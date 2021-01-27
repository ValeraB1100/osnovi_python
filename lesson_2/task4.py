a = input("напишите что-нибудь хорошее: ")
lst = a.split(" ")
n = 1
for i in lst:
    if int(len(i)) > 10:
        print(f"{n} {i[0:11]}")
        n+=1
    else:
        print(f"{n} {i}")
        n+=1
