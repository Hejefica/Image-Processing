import numpy as np
import cv2
from ImgResize import image_resize

imgori = cv2.imread("CETI.jpg")

def resize(imagen, ancho, alto):
    dim = (ancho, alto)
    img_resized = cv2.resize(imagen, dim, interpolation = cv2.INTER_AREA)
    return img_resized

def translation(imagen, desp_x, desp_y):
    dimension_original = imagen.shape
    M = np.float32([
         [1, 0, desp_x],
         [0, 1, desp_y]
         ])
    img_trasl = cv2.warpAffine(imagen, M, (dimension_original[1], dimension_original[0]))
    return img_trasl

def rotation (imagen, angulo):
    altura, ancho = imagen.shape[:2]
    centro = (altura/2, ancho/2)
    matriz_rotacion = cv2.getRotationMatrix2D(center=centro, angle=angulo, scale=1)
    rotated_image = cv2.warpAffine(imgori, M=matriz_rotacion, dsize=(ancho, altura))
    return rotated_image

def flip(imagen, eje):
    img_volteada = cv2.flip(imagen, eje)
    return img_volteada    

img_resized = resize(imgori, 300, 240)
img_trasl = translation(imgori, 56, 20)
img_rotated = rotation(imgori, -12)
img_flipped = flip(imgori, 1)


ImgSize = 220
cv2.imshow("Original Image", image_resize(imgori, Height = ImgSize))
cv2.moveWindow('Original Image', 20, 20)
cv2.imshow("Resized Image", image_resize(img_resized, Height = ImgSize))
cv2.moveWindow('Resized Image', 300, 20)
cv2.imshow("Traslated Image", image_resize(img_trasl, Height = ImgSize))
cv2.moveWindow('Traslated Image', 580, 20)
cv2.imshow("Rotated Image", image_resize(img_rotated, Height = ImgSize))
cv2.moveWindow('Rotated Image', 860, 20)
cv2.imshow("Fliped Image", image_resize(img_flipped, Height = ImgSize))
cv2.moveWindow('Fliped Image', 1140, 20)

cv2.waitKey(0)
cv2.destroyAllWindows() 