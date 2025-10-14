n = input("Zadaj číslo: ")
dlzka = len(n)

if dlzka % 2 == 1:
    stredna = int(n[dlzka // 2])
else:
    stred1 = int(n[dlzka // 2 - 1])
    stred2 = int(n[dlzka // 2])
    stredna = (stred1 + stred2) / 2

print("Stredná cifra:", stredna)
