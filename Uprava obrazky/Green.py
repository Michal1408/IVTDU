from PIL import Image
pic = Image.open("Epstein.jpg")
pixel = pic.load()
for x in range(pic.size[0]):
    for y in range(pic.size[1]):
        temp = pixel[x,y]
        pixel[x,y] = (0, temp[0],0)
pic.show()
