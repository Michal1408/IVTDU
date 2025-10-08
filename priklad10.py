N=int(input("N:"))
for i in range(1,N+1):
    if N+1-i !=1:
        print(N+1-i,end=",")
    else:
        print(1)