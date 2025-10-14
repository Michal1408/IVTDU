N=int(input("N="))
sci=0
while N>0:
    sci=N%10+sci
    N//=10
print(sci)