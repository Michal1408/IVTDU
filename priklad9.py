N=int(input('N='))
cif=0
while N>0:
    cif=cif+1
    N//=10
if cif%2==0:
    print("Je symetricke")
else:
    print("nie je symetricke")
#NEVIEM CO TO JE SYMETRICKE CISLO
