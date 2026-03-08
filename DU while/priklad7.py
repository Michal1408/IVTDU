n = int(input("Zadaj číslo: "))
hod=0
dvojka=0
while n>0:
    hod= n%2
    dvojka = dvojka*10 +hod
    n//=2
print(str(dvojka)[::-1])
