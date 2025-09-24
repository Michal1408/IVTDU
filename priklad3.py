x = int(input("X="))
print("teraz interval")
a = int(input("A="))
b = int(input("B="))
if a<=x<=b or b<=x<=a or a==b==x:
    print("patri do intervalu")
else:
    print("nepatri do intervalu")