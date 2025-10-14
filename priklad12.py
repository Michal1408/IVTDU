n = int(input("Zadaj číslo: "))
print("Delitelia cisla", n, "su:", end=" ")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")