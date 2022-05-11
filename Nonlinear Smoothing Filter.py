import cv2
import numpy as np
from ImgResize import image_resize

Img = cv2.imread('CETI-B&W.jpg')

def SaltnPepperNoise(Img, Signal):
    Height, Width = Img.shape[: 2]
    Copy = Img.copy()
    Npix = Height * Width
    Npoints = int (Npix * (1 - Signal))
    for i in range (Npoints):
        RandX = np.random.randint (1, Height-1)
        RandY = np.random.randint (1, Width-1)
        if np.random.random () <= 0.5:
            Copy[RandX, RandY] = 0
        else:
            Copy[RandX, RandY] = 255
    return Copy

def SaltNoise(Img, Signal):
    Height, Width = Img.shape[: 2]
    Copy = Img.copy()
    Npix = Height * Width
    Npoints = int (Npix * (1 - Signal))
    for i in range (Npoints):
        RandX = np.random.randint (1, Height-1)
        RandY = np.random.randint (1, Width-1)
        if np.random.random () <= 0.5:
            pass
        else:
            Copy[RandX, RandY] = 255
    return Copy

SaltnPepperImg = SaltnPepperNoise(Img, 0.8)
SaltImg = SaltNoise(Img, 0.8)
MedianImg= cv2.medianBlur(SaltnPepperImg, 5)
kernel = np.ones((5,5), np.uint8) #Filtro Minimo
MinImg = cv2.erode(SaltImg, kernel)

cv2.imshow("Original Image", image_resize(Img, height = 350))
cv2.moveWindow('Original Image', 20, 20)
cv2.imshow("Salt & Pepper Noise", image_resize(SaltnPepperImg, height = 350))
cv2.moveWindow('Salt & Pepper Noise', 475, 20)
cv2.imshow("Median Filter", image_resize(MedianImg, height = 350))
cv2.moveWindow('Median Filter', 930, 20)
cv2.imshow("Salt Noise", image_resize(SaltImg, height = 350))
cv2.moveWindow('Salt Noise', 20, 420)
cv2.imshow("Minimum Filter",image_resize(MinImg, height = 350))
cv2.moveWindow('Minimum Filter', 475, 420)

cv2.waitKey(0)
cv2.destroyAllWindows()