import numpy as np

def inv_logtransform(img):
    temp = np.zeros(img.shape).astype(np.uint8)
    c=255/np.log(1+255)
    for i in range (len (img)):
        for j in range (len (img[0])):
            pixel = img[i][j]
            pixel =( 2.5 ** (pixel/c))-1
            temp[i,j]= pixel
    return temp