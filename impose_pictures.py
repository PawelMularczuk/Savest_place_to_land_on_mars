from PIL import Image

img = Image.open('./pix/mars_og_crop.png')

img2 = Image.open('./pix/mars_layer_2.png')

img.paste(img2, mask=img2)

img.save('./pix/Mars_save_place.png')