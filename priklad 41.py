import tkinter

root = tkinter.Tk()

platno = tkinter.Canvas(root, width=420, height=150, bg='white')
platno.pack()

def nakresli():
    for index in range(len(zoznam_farieb)):
        platno.create_rectangle(
            zacx + index * strana,
            zacy,
            zacx + index * strana + strana - 2,
            zacy + strana - 2,
            fill=zoznam_farieb[index],
            outline=''
        )

def kliknutie(event):
    if zacy < event.y < zacy + strana:
        cislo = (event.x - zacx) // strana
        if 0 <= cislo < len(zoznam_farieb):
            print(cislo)
            id_studenta = vstup.get()
            if id_studenta != '':
                f = open('vyber_jedla.txt', 'a')
                f.write(id_studenta + ' ' + pismena[cislo] + '\n')
                f.close()

platno.create_text(210, 20, text='VÝBER JEDLA', font='Arial 20', fill='red')
f = open('vyber_jedla.txt', 'w')
f.close()
zoznam_farieb = ['green', 'red', 'blue', 'orange']
pismena = 'zcmo'
zacx, zacy, strana = 10, 40, 100
nakresli()
platno.bind('<Button-1>', kliknutie)
popis = tkinter.Label(root, text='kód študenta:')
popis.pack()
vstup = tkinter.Entry(root)
vstup.pack()

root.mainloop()