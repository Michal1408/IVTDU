from PIL import Image
pic = Image.open("../files/Epstein.jpg")
pixel = pic.load()
for x in range(pic.size[0]):
    for y in range(pic.size[1]):
        temp = pixel[x,y]
        pixel[x,y] = (temp[0], 0, 0)
pic.show()
