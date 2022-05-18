import numpy as np
import cv2
from ImgResize import image_resize

Img = cv2.imread("CETI.jpg")

def resize(Img, Width, Height):
    dim = (Width, Height)
    ResizedImg = cv2.resize(Img, dim, interpolation = cv2.INTER_AREA)
    return ResizedImg

def Traslation(Img, X, Y):
    OriginalShape = Img.shape
    M = np.float32([
         [1, 0, X],
         [0, 1, Y]
         ])
    TraslatedImg = cv2.warpAffine(Img, M, (OriginalShape[1], OriginalShape[0]))
    return TraslatedImg

def Rotation (Img, Angle):
    Height, Width = Img.shape[:2]
    Center = (Height/2, Width/2)
    RotationMatrix = cv2.getRotationMatrix2D(center=Center, angle=Angle, scale=1)
    RotatedImg = cv2.warpAffine(Img, M=RotationMatrix, dsize=(Width, Height))
    return RotatedImg

def flip(Img, Axis):
    FlippedImg = cv2.flip(Img, Axis)
    return FlippedImg    

ResizedImg = resize(Img, 300, 240)
TraslatedImg = Traslation(Img, 56, 20)
RotatedImg = Rotation(Img, -12)
FlippedImg = flip(Img, 1)

ImgSize = 220
cv2.imshow("Original Image", image_resize(Img, Height = ImgSize))
cv2.moveWindow('Original Image', 20, 20)
cv2.imshow("Resized Image", image_resize(ResizedImg, Height = ImgSize))
cv2.moveWindow('Resized Image', 300, 20)
cv2.imshow("Traslated Image", image_resize(TraslatedImg, Height = ImgSize))
cv2.moveWindow('Traslated Image', 580, 20)
cv2.imshow("Rotated Image", image_resize(RotatedImg, Height = ImgSize))
cv2.moveWindow('Rotated Image', 860, 20)
cv2.imshow("Fliped Image", image_resize(FlippedImg, Height = ImgSize))
cv2.moveWindow('Fliped Image', 1140, 20)

cv2.waitKey(0)
cv2.destroyAllWindows() 