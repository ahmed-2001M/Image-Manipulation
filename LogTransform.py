import numpy as np
import matplotlib.pyplot as plt

def logtransform(img):
    temp = np.zeros(img.shape).astype(np.uint8)
    c=255/np.log(1+255)
    for i in range (len (img)):
        for j in range (len (img[0])):
            pixel = img[i][j]
            pixel =c* np.log(1+pixel)
            temp[i,j]= pixel

    return temp