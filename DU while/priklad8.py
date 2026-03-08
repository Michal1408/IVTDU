N = int((input("Zadaj číslo: ")))
n = str(N)[::-1]
pocet=len(n)
cislo=0
Cislo=0
while N>0:
    for i in range(0, pocet):
        cislo=int(n[i])
        Cislo=cislo*2**i+Cislo
    N=0
print(Cislo)