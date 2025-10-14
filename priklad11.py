n = int(input("Zadaj číslo: "))
delitel = 2
print("Prvočíselný rozklad:", end=" ")
while n > 1:
    if n % delitel == 0:
        print(delitel, end=" ")
        n = n // delitel
    else:
        delitel = delitel + 1