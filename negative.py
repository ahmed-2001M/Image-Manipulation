


import numpy as np


def negative(img):
    temp = np.zeros(img.shape).astype(np.uint8)
    for i in range (len (img)):
        for j in range (len (img[0])):
            pixel = img[i][j]
            pixel = 255-pixel
            temp[i][j]= pixel
    return temp