import cv2

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