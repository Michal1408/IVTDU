a = int(input("Zadaj číslo: "))
prve = 0
druhe = 0
pozicia = 1
while a > 0:
    cifra = a % 10           # zoberie poslednú cifru
    if pozicia % 2 == 0:     # párna pozícia (odzadu)
        prve = prve * 10 + cifra
    else:                    # nepárna pozícia (odzadu)
        druhe = druhe * 10 + cifra
    a //= 10                 # odrežeme poslednú cifru
    pozicia += 1
print("Neparne miesta:", prve)
print("Parne miesta:", druhe)
print("Moznost A")
prve = int(str(prve)[::-1])
druhe = int(str(druhe)[::-1])
print(druhe)