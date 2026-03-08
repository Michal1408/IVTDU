slovo = input()
preklad =""
def humtobird(slovo):
    import random
    vysledok=""
    sam = "aeiouy"
    for i in slovo:
        if i in sam:
            vysledok += 3*i
        else:
            vysledok += i+random.choice(sam)
    return vysledok
humtobird(slovo)
def birdtohum(vysledok):
    n=0
    while n<len(humtobird(slovo)):
        for i in vysledok:
            sam = "aeiouy"
            spol = "bcdfghjklzxcvbnm"
            vysledok2 =""
            if i in sam:
                vysledok2 += i
                n += 2
            else:
                vysledok2 += i
                n += 1
    return vysledok2
print(birdtohum(humtobird(slovo)))