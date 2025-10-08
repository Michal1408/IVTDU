z=int(input("zaciatok:"))
k=int(input("koniec:"))
delit=0
for i in range(z,k+1):
    if i%8==0:
        delit +=1
print(delit)