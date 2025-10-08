N=int(input("N:"))
if N>4:
    for i in range(5,N+1,2):
        print(i, end=",")
else:
    print("Zadaj cislo N>4")