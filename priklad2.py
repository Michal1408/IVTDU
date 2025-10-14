N=int(input('N='))
par=0
cif=0
while N>0:
    cif=N%10
    if cif%2==0:
        par=par+1
    N//=10
print(par)