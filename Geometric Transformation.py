import numpy as np
import cv2
from ImgResize import image_resize

Img = cv2.imread("CETI.jpg")

def resize(Img, Width, Height):
    Dimention = (Width, Height)
    ResizedImg = cv2.resize(Img, Dimention, interpolation = cv2.INTER_AREA)
    return ResizedImg

def Translation(Img, X, Y):
    ImgShape = Img.shape
    Matrix = np.float32([[1, 0, X],
                         [0, 1, Y]])
    TranslatedImg = cv2.warpAffine(Img, Matrix, (ImgShape[1], ImgShape[0]))
    return TranslatedImg

def Rotation(Img, Angle):
    Height, Width = Img.shape[:2]
    RotationMatrix = cv2.getRotationMatrix2D(center = (Height / 2, Width / 2), angle = Angle, scale = 1)
    RotatedImg = cv2.warpAffine(Img, M = RotationMatrix, dsize = (Width, Height))
    return RotatedImg

def flip(Img, Axis):
    FlippedImg = cv2.flip(Img, Axis)
    return FlippedImg    

ResizedImg = resize(Img, 375, 295)
TranslatedImg = Translation(Img, 500, 500)
RotatedImg = Rotation(Img, 45)
FlippedImg = flip(Img, 1)

ImgSize = 220
cv2.imshow("Original Image", image_resize(Img, Height = ImgSize))
cv2.moveWindow('Original Image', 20, 20)
cv2.imshow("Resized Image", ResizedImg)
cv2.moveWindow('Resized Image', 300, 20)
cv2.imshow("Traslated Image", image_resize(TranslatedImg, Height = ImgSize))
cv2.moveWindow('Traslated Image', 680, 20)
cv2.imshow("Rotated Image", image_resize(RotatedImg, Height = ImgSize))
cv2.moveWindow('Rotated Image', 963, 20)
cv2.imshow("Fliped Image", image_resize(FlippedImg, Height = ImgSize))
cv2.moveWindow('Fliped Image', 1234, 20)

cv2.waitKey(0)
cv2.destroyAllWindows() 