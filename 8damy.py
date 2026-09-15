import PIL
from PIL import Image,ImageDraw
import random

chessboard = []
vsetky_riesenia = []
counter = 0
size_sq = 50
number = 8
width = size_sq * number
height = size_sq * number
col_b =  (0, 0, 0)
col_w = (255, 255, 255)

def createImage():
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    for riadok in range(number):
        for stlpec in range(number):
            x1 = size_sq * stlpec
            y1 = size_sq * riadok
            x2 = x1 + size_sq
            y2 = y1 + size_sq
            if (riadok + stlpec) % 2 == 1:
                color = col_w
            else:
                color = col_b
            draw.rectangle([x1,y1,x2,y2], fill=color)
createImage()

def create_board ():
    global chessboard
    #chessboard = [row] * 8  # mega pruser takto to nikdy nerob !!!!!
    for i in range (8):
        row = [0] * 8
        chessboard.append(row)

def check_it (x, y):
    for i in range (0, 8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8):    #y
        for o in range(0,8):    #x
            if i+o == x+y:
                if chessboard[i][o] == 1:
                    return False
            if i-o == y-x:
                if chessboard[i][o] == 1:
                    return False
    return True

def queens (n):
    global chessboard , counter , vsetky_riesenia
    if n == 8:
        counter += 1
        # ulozim si toto riesenie do zoznamu vsetkych rieseni
        jedno_riesenie = []
        for riadok in chessboard:
            jedno_riesenie.append(riadok[:])
        vsetky_riesenia.append(jedno_riesenie)
        print(chessboard)
        print(counter)
        print('-----------------------------')
    else:
        for i in range (8):
            if check_it(i,n):
                chessboard[n][i] = 1
                queens(n+1)
                chessboard[n][i] = 0

def uprav_obrazok_damy ():
    dama = Image.open('queen.png')
    dama = dama.convert('RGB')
    pixely = dama.load()
    w = dama.size[0]
    h = dama.size[1]
    for y in range(h):
        for x in range(w):
            r, g, b = pixely[x, y]
            priemer = (r + g + b) / 3
            if priemer < 128:
                pixely[x, y] = (0, 0, 0)
            else:
                pixely[x, y] = (255, 255, 255)
    ImageDraw.floodfill(dama, (0, 0), (0, 255, 0), thresh=10)
    dama = dama.convert('RGBA')
    pixely = dama.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixely[x, y]
            if r == 0 and g == 255 and b == 0:
                pixely[x, y] = (255, 255, 255, 0)
    dama = dama.resize((size_sq, size_sq))
    return dama

def nakresli_riesenie_s_damami ():
    riesenie = random.choice(vsetky_riesenia)
    obrazok_damy = uprav_obrazok_damy()
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    for riadok in range(number):
        for stlpec in range(number):
            x1 = size_sq * stlpec
            y1 = size_sq * riadok
            x2 = x1 + size_sq
            y2 = y1 + size_sq
            if (riadok + stlpec) % 2 == 1:
                color = col_w
            else:
                color = col_b
            draw.rectangle([x1,y1,x2,y2], fill=color)
    image = image.convert('RGBA')
    for riadok in range(number):
        for stlpec in range(number):
            if riesenie[riadok][stlpec] == 1:
                x1 = size_sq * stlpec
                y1 = size_sq * riadok
                image.paste(obrazok_damy, (x1, y1), obrazok_damy)
    image.show()


create_board()
queens(0)
nakresli_riesenie_s_damami()
