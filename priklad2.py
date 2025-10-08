

N = int(input("N="))
print("Moznost a:")
for i in range(1,N+1):
    print(i)
print("Moznost b:")
for i in range(1,N+1):
    if i<N:
        print(i, end=",")
    else:
        print(i)