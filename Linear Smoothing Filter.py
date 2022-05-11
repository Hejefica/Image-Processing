import cv2
import numpy as np
from ImgResize import image_resize

BnWImg = cv2.imread('CETI-B&W.jpg')
GaussianImg = cv2.imread('CETI-Gaussian.png')

def ImgNoise(Img, Signal):
    Height, Width = Img.shape[: 2]
    Copy = Img.copy()
    Npix = Height * Width
    Npoints = int(Npix * (1 - Signal))
    for i in range(Npoints):
        RandX = np.random.randint(1, Height - 1)
        RandY = np.random.randint(1, Width - 1)
        if np.random.random() <= 0.5:
            Copy[RandX, RandY] = 0
        else:
            Copy[RandX, RandY] = 255
    return Copy

SaltnPepperImg = ImgNoise(BnWImg, 0.8)
AvgFilter = cv2.blur(SaltnPepperImg, (7, 7))
GaussianFilter = cv2.GaussianBlur(GaussianImg, (13, 13), 0)

cv2.imshow("Black & White Image", image_resize(BnWImg, Height = 350))
cv2.moveWindow('Black & White Image', 20, 20)
cv2.imshow("Salt & Pepper Image", image_resize(SaltnPepperImg, Height = 350))
cv2.moveWindow('Salt & Pepper Image', 475 ,20)
cv2.imshow("Average Filter", image_resize(AvgFilter, Height = 350))
cv2.moveWindow('Average Filter', 930, 20)
cv2.imshow("Gaussian Image", image_resize(GaussianImg, Height = 350))
cv2.moveWindow('Gaussian Image', 20, 420)
cv2.imshow("Gaussian Filter", image_resize(GaussianFilter, Height = 350))
cv2.moveWindow('Gaussian Filter', 475 ,420)

cv2.waitKey(0)
cv2.destroyAllWindows()