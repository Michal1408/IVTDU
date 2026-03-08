from PIL import Image
pic = Image.open("Epstein.jpg")
pixel = pic.load()
for x in range(pic.size[0]):
    for y in range(pic.size[1]):
        temp = pixel[x,y]
        if temp[0]<=128 and temp[1]<=128 and temp[2]<=128:
            pixel[x,y] = (0,0,0)
        else:
            pixel[x,y] = (255,255,255)
pic.show()
