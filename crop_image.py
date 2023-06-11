import cv2
# import matplotlib.pyplot as plt

# importuję zdjęcie
image = cv2.imread('./pix/mars_og.png')

# za pomocą pixeli wyznaczam jaki obszar zdjęcia mnie interesuje
cropped = image[60:1060,33:1871]


# zapisuję potrzebny fragment
cv2.imwrite('./pix/mars_og_crop.png', cropped)

# cv2.imshow("Cropped", cropped)
# cv2.waitKey(0)


image_2 = cv2.imread('./pix/mars_save_place_to_land.png')

cropped_2 = image_2[60:1060,33:1871]

cv2.imwrite('./pix/mars_save_place_to_land_crop.png', cropped_2)