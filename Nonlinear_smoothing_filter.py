import cv2
import numpy as np

img = cv2.imread("CETI.jpg")

MedianFilter = cv2.medianBlur(img, 5)

def original(i, j, k, ksize, img):
    x1 = y1 = -ksize // 2
    x2 = y2 = ksize + x1
    temp = np.zeros(ksize * ksize)
    count = 0
    for m in range(x1, x2):
        for n in range(y1, y2):
            if i + m < 0 or i + m > img.shape[0] - 1 or j + n < 0 or j + n > img.shape[1] - 1:
                temp[count] = img[i, j, k]
            else:
                temp[count] = img[i + m, j + n, k]
                count += 1
    return temp

def max_min_functin(ksize, img, flag):
    img0 = img
    for i in range(0, img.shape[0]):
        for j in range(2, img.shape[1]):
            for k in range(img.shape[2]):
                temp = original(i, j, k, ksize, img0)
            if flag == 0:
                img[i, j, k] = np.max(temp)
            elif flag == 1:
                img[i, j, k] = np.min(temp)
    return img

MinFilter = max_min_functin(3, img, 1)
MaxFilter = max_min_functin(3, img, 0)

#Resize Image Output for Windowed View
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    #Initialize the dimensions of the image to be resized and grab the image size
    dim = None
    (h, w) = image.shape[:2]
    #If both the width and height are None, then return the original image
    if width is None and height is None:
        return image
    #Check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    #Otherwise, the height is None
    else:
        #Calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    #Resize the image
    resized = cv2.resize(image, dim, interpolation = inter)
    #Return the resized image
    return resized

#Shows Images
cv2.imshow('Original', image_resize(img, height = 250))
cv2.moveWindow('Original', 20,20)
cv2.imshow('Median Blur', image_resize(MedianFilter, height = 250))
cv2.moveWindow('Median Blur', 20,365)
cv2.imshow('Minimum Blur', image_resize(MinFilter, height = 250))
cv2.moveWindow('Minimum Blur', 400,365)
cv2.imshow('Maximum Blur', image_resize(MaxFilter, height = 250))
cv2.moveWindow('Maximum Blur', 400,20)

WebCam = cv2.VideoCapture(0)
while(True):
    ret, feed = WebCam.read()
    cv2.imshow('Original Webcam', image_resize(feed, height = 250))
    cv2.moveWindow('Original Webcam', 780,20)
    cv2.imshow('Median Blur Webcam', image_resize(cv2.medianBlur(feed, 5), height = 250))
    cv2.moveWindow('Median Blur Webcam', 1160,365)
    cv2.imshow('Minimum Blur Webcam', image_resize(max_min_functin(3, feed, 1), height = 250))
    cv2.moveWindow('Minimum Blur Webcam', 780,365)
    cv2.imshow('Maximum Blur Webcam', image_resize(max_min_functin(3, feed, 0), height = 250))
    cv2.moveWindow('Maximum Blur Webcam', 1160,20)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
WebCam.release()

cv2.waitKey('q')
cv2.destroyAllWindows()