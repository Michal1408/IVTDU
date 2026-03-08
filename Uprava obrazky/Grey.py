from PIL import Image
pic = Image.open("Epstein.jpg")
pixel = pic.load()
for x in range(pic.size[0]):
    for y in range(pic.size[1]):
        temp = pixel[x,y]
        temp = int((temp[0]+temp[1]+temp[2])/3)
        pixel[x,y] = (temp,temp,temp)
pic.show()
