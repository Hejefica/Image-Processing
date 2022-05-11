import cv2
import numpy as np
from ImgResize import image_resize

Img = cv2.imread("CETI.jpg")
GrayScale = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
GaussianBlurImg = cv2.GaussianBlur(GrayScale, (3, 3), 0)

SobelImgX = cv2.Sobel(GaussianBlurImg, cv2.CV_8U, 1, 0, ksize=3)
SobelImgY = cv2.Sobel(GaussianBlurImg, cv2.CV_8U, 0, 1, ksize=3)
SobelImg = SobelImgX + SobelImgY

KernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
KernelY = np.array([[-1, 0, 1], [-1,0,1], [-1, 0, 1]])
PrewittImgX = cv2.filter2D(GaussianBlurImg, -1, KernelX)
PrewittImgY = cv2.filter2D(GaussianBlurImg, -1, KernelY)

LaplaceImg = cv2.Laplacian(GaussianBlurImg, -1, ksize = 3)
ImgSize = 220
cv2.imshow("Original Image", image_resize(Img, Height = ImgSize))
cv2.moveWindow('Original Image', 20, 20)
cv2.imshow("Black and white Image", image_resize(GrayScale, Height = ImgSize))
cv2.moveWindow('Black and white Image', 300, 20)
cv2.imshow("Gaussian Image", image_resize(GaussianBlurImg, Height = ImgSize))
cv2.moveWindow('Gaussian Image', 580, 20)
cv2.imshow("Sobel X", image_resize(SobelImgX, Height = ImgSize))
cv2.moveWindow('Sobel X', 860, 20)
cv2.imshow("Sobel Y", image_resize(SobelImgY, Height = ImgSize))
cv2.moveWindow('Sobel Y', 1140, 20)
cv2.imshow("Sobel", image_resize(SobelImg, Height = ImgSize))
cv2.moveWindow('Sobel', 20, 350)
cv2.imshow("Prewitt X", image_resize(PrewittImgX, Height = ImgSize))
cv2.moveWindow('Prewitt X', 300, 350)
cv2.imshow("Prewitt Y", image_resize(PrewittImgY, Height = ImgSize))
cv2.moveWindow('Prewitt Y', 580, 350)
cv2.imshow("Prewitt", image_resize(PrewittImgX + PrewittImgY, Height = ImgSize))
cv2.moveWindow('Prewitt', 860, 350)
cv2.imshow("Laplace", image_resize(LaplaceImg, Height = ImgSize))
cv2.moveWindow('Laplace', 1140, 350)

cv2.waitKey(0)
cv2.destroyAllWindows()