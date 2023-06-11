import cv2
import numpy as np

# wczytuję i przypisuje zdjęcie topograficzne do zmniennej 
img = cv2.imread('pix/mercat.jpg', 1,)


# Konwertuję zdjęcie z RGB na HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Wybieram zakres kolorów który mnie interesuje
lower_yellow = np.array([30, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Tworzę maskę które wyświetli tylko podane kolory
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# łącze ze sobą dwa te same zdjęcia i zagnieżdżam w nich maskę
result = cv2.bitwise_and(img, img, mask=mask)

# Za pomocą maski wybieram kolory które chcę zamienić na czerwony
result[mask > 0] = [0,0,255]


# zapisuję zmodyfikowane zdjęcie
cv2.imwrite('./pix/mars_save_place_to_land.png', result)

