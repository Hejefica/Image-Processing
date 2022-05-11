import cv2
import numpy as np
from ImgResize import image_resize

img = cv2.imread("CETI.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
img_sobel = img_sobelx + img_sobely

#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

#Laplaciano
img_lpc = cv2.Laplacian(img_gaussian, -1, ksize=3)
size = 220
cv2.imshow("Original Image", image_resize(img, height = size))
cv2.moveWindow('Original Image', 20, 20)
cv2.imshow("Black and white Image", image_resize(gray, height = size))
cv2.moveWindow('Black and white Image', 300, 20)
cv2.imshow("Gaussian Image", image_resize(img_gaussian, height = size))
cv2.moveWindow('Gaussian Image', 580, 20)
cv2.imshow("Sobel X", image_resize(img_sobelx, height = size))
cv2.moveWindow('Sobel X', 860, 20)
cv2.imshow("Sobel Y", image_resize(img_sobely, height = size))
cv2.moveWindow('Sobel Y', 1140, 20)
cv2.imshow("Sobel", image_resize(img_sobel, height = size))
cv2.moveWindow('Sobel', 20, 350)
cv2.imshow("Prewitt X", image_resize(img_prewittx, height = size))
cv2.moveWindow('Prewitt X', 300, 350)
cv2.imshow("Prewitt Y", image_resize(img_prewitty, height = size))
cv2.moveWindow('Prewitt Y', 580, 350)
cv2.imshow("Prewitt", image_resize(img_prewittx + img_prewitty, height = size))
cv2.moveWindow('Prewitt', 860, 350)
cv2.imshow("Laplace", image_resize(img_lpc, height = size))
cv2.moveWindow('Laplace', 1140, 350)

cv2.waitKey(0)
cv2.destroyAllWindows()