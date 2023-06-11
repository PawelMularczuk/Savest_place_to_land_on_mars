from PIL import Image

# importuję zdjęcie mapy topograficznej marsa
pic = Image.open("./pix/mercat.jpg")

# zmieniam barwy mapy na "naturalne kolory marsa"
for x in range(pic.size[0]):
    for y in range(pic.size[1]):
        r, g, b = pic.getpixel((x,y))
        tr = int(.393*r + .769*g + .189*b)
        tg = int(.349*r + .686*g + .168*b)
        tb = int(.272*r + .534*g + .131*b)    
        pic.putpixel((x,y), (tr, tg, tb))


# Zapisuje zdjęcie marsa
pic.save('./pix/mars_og.png')

pic.show()






